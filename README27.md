# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1facf4a2-17e1-3f96-bacb-bfb44ed216ba | -12.47753 | -54.42597 | 2025-06-21 05:25:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 53622f89-4212-3669-9998-2e16a70aacb3 | -11.57032 | -54.56733 | 2025-06-21 05:25:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c36a30c-16f9-3c1f-a9ac-b18226a03911 | -11.95067 | -58.75857 | 2025-06-21 05:25:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aefdc7ca-d7f6-33c6-89cd-552c8904919b | -11.87271 | -54.67851 | 2025-06-21 05:25:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 344a308b-9bf4-3d3a-8efb-c5666bea66ac | -11.65528 | -60.12128 | 2025-06-21 05:25:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 898a81c1-e0ad-39f4-a64b-0864ef9c7bc9 | -13.23429 | -49.83735 | 2025-06-21 05:25:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 711ab73a-7611-3403-8769-383e94b230dc | -14.07314 | -53.38 | 2025-06-21 05:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 34960b69-7ef7-38ed-9deb-32071447a662 | -10.23365 | -64.35949 | 2025-06-21 05:25:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4c09660-03e4-36cb-bcbb-dcaa84b317c6 | -11.94351 | -58.75743 | 2025-06-21 05:25:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ed17ffa5-1de6-3111-be85-16d79ab2ce4b | -11.91544 | -54.81405 | 2025-06-21 05:25:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca3067f0-06cd-3584-b2de-77d7906bf7c3 | -12.42656 | -54.86814 | 2025-06-21 05:25:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c0ced0e-9dad-386b-abfc-e8a39eb740c3 | -12.9735 | -54.68647 | 2025-06-21 05:25:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 90411555-4826-3854-9899-6f2d0806f453 | -12.42525 | -54.87777 | 2025-06-21 05:25:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05aea2b6-db9a-3859-bd7a-57d50abb869d | -13.24077 | -49.838 | 2025-06-21 05:25:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1f96bd31-79e0-3640-bcd1-beb4da520e78 | -12.57457 | -58.37477 | 2025-06-21 05:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bbdd4a58-2e6a-3d86-8f66-98047d01bab5 | -11.9429 | -58.76159 | 2025-06-21 05:25:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68dc7597-1619-3a4b-ba85-b99f4ca4dbed | -13.10028 | -52.29414 | 2025-06-21 05:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49941145-151d-3475-9985-9962e14c365e | -21.68944 | -49.50295 | 2025-06-21 05:25:00 | NOAA-20 | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 9a240eef-d106-3b6c-8b3c-bb5cc3f54438 | -11.52781 | -56.97561 | 2025-06-21 05:25:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96a63464-0642-3cb0-b2e9-ad1476846c66 | -10.23434 | -64.3554 | 2025-06-21 05:25:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97fc998f-bcd1-3704-8ba8-587e41b434f2 | -12.57627 | -58.38203 | 2025-06-21 05:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09e8ab3e-8d36-3258-84f7-48e1eabe4d5b | -12.42591 | -54.87009 | 2025-06-21 05:25:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c08df874-509f-3035-af4d-091185307a9a | -11.78675 | -57.24086 | 2025-06-21 05:25:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 27.7 |
| cb5252b8-ea40-3eef-a901-501fdfa6c4ee | -12.57392 | -58.3792 | 2025-06-21 05:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b16d8da-aee1-3c27-8f7f-db3c97635203 | -21.6961 | -49.51087 | 2025-06-21 05:25:00 | NOAA-20 | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 96773c61-4db8-3e27-b1a2-ed99706a048a | -11.53643 | -56.97161 | 2025-06-21 05:25:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 15f24464-6868-3e9f-a6c6-ac622b8760d7 | -11.91482 | -54.81881 | 2025-06-21 05:25:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b5316a8-9bcc-3ce0-be59-c2c266c39319 | -12.50956 | -58.35595 | 2025-06-21 05:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a55fe0dc-2111-3c10-9158-3787ecbaebe8 | -13.29212 | -57.08481 | 2025-06-21 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7acab8f6-6e95-3a32-a2fe-8aac5fda8445 | -13.09432 | -52.29708 | 2025-06-21 05:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28e651fb-6372-3230-aee3-959ab348a0bc | -12.52266 | -57.20627 | 2025-06-21 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ed7ef007-4016-3292-86fe-31f87443c1da | -13.23464 | -49.8385 | 2025-06-21 05:25:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 4c319322-474f-3421-b503-1f90b9e38450 | -11.78744 | -57.23592 | 2025-06-21 05:25:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 35acde21-eefa-3c3d-8506-58b07c07ac46 | -11.5357 | -56.97675 | 2025-06-21 05:25:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c4279c16-05e4-3ff6-a9b7-cfc010177b0c | -11.94894 | -58.74548 | 2025-06-21 05:25:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 96daee49-e9e2-3d2f-b9a8-6f557c5c87ed | -11.53176 | -56.97619 | 2025-06-21 05:25:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e666cb0-c3bb-3acc-b336-72c17922add8 | -11.87336 | -54.67367 | 2025-06-21 05:25:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 48246e99-8959-3a44-a960-92f5f3596e27 | -12.42591 | -54.87296 | 2025-06-21 05:25:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6505f09-b54d-3d56-8713-563c7161c047 | -12.47589 | -60.13616 | 2025-06-21 05:25:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 43cc2948-495a-31f8-b3c5-1968873848f9 | -12.2821 | -50.10397 | 2025-06-21 05:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 622d754b-dc65-35e4-92ba-14bc4e969df0 | -11.70334 | -54.50343 | 2025-06-21 05:25:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 568261f7-274c-3b33-b326-f084ea84b740 | -11.57561 | -54.56305 | 2025-06-21 05:25:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f7fc0548-7cd9-3e4a-a4a8-d4edf9fdcdc6 | -13.14443 | -56.80511 | 2025-06-21 05:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 025a6f7b-2c54-36fe-b13e-e88f71351a34 | -11.94412 | -58.75327 | 2025-06-21 05:25:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8c723e6e-bb8e-35c0-b69c-e62e10540140 | -12.28781 | -50.10981 | 2025-06-21 05:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 626d6528-3519-3141-bacd-5fcd2d2000b3 | -11.86873 | -54.67305 | 2025-06-21 05:25:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a1ea1b6a-483e-337c-bbfc-f6db9dd48574 | -11.94474 | -58.7491 | 2025-06-21 05:25:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2ebfd5b4-7b40-3733-bc3a-bfeb3a85bc92 | -12.47683 | -54.42421 | 2025-06-21 05:25:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| a7e027e8-2e7b-30d8-8151-72de0eac594c | -12.97144 | -54.68348 | 2025-06-21 05:25:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d4989b12-7514-3cd3-9645-b9fd8b5f331d | -11.94115 | -58.74857 | 2025-06-21 05:25:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 496b441b-e7fc-31e3-95c9-08b0da0912bc | -12.97417 | -54.6814 | 2025-06-21 05:25:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d544467f-15d4-385b-9eb7-a0ddebc9ffea | -11.95365 | -58.76324 | 2025-06-21 05:25:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 49dde1fd-0b9f-3b75-a490-c051807a2ccc | -11.94771 | -58.75384 | 2025-06-21 05:25:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f41c9342-7c70-3d58-ba96-b2e361e10cde | -14.03786 | -53.36561 | 2025-06-21 05:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 326a23ae-be53-37e9-b05b-c010b34a49e1 | -13.65758 | -53.94205 | 2025-06-21 05:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3221c694-3765-3f5b-a5fc-f9145b4da057 | -13.04422 | -53.71595 | 2025-06-21 05:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 114e338a-e211-340e-84fe-475f43ec1e7c | -12.57153 | -58.36983 | 2025-06-21 05:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce7056f0-0876-3726-b20e-2573a275a926 | -12.88696 | -56.98363 | 2025-06-21 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| baa7c9a7-ef32-32ab-bb5b-f03cefe5e84c | -13.03957 | -53.71236 | 2025-06-21 05:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| fa6408a6-efaa-3d12-8c8a-55f22f71bf62 | -11.79133 | -57.23647 | 2025-06-21 05:25:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 045a5c24-9076-3b54-932c-421c88e966e5 | -12.13126 | -54.66861 | 2025-06-21 05:25:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3ac77dbe-672f-3136-9b56-2466e7fb2832 | -21.4427 | -54.57301 | 2025-06-21 05:25:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b647ea4-d9d8-3515-9626-77d9fede08cf | -12.57219 | -58.36536 | 2025-06-21 05:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed1dfa93-a592-3415-a63b-1e458196b941 | -11.88326 | -54.67005 | 2025-06-21 05:25:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 54bd5bec-2600-3b8a-a234-f5f3b05760ea | -13.09984 | -52.29783 | 2025-06-21 05:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17b3371c-1811-3b8c-835e-f24eeee1e79f | -12.05537 | -63.7788 | 2025-06-21 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c845359d-e4b1-3eea-8da9-3cdde15ccc59 | -12.30767 | -63.7396 | 2025-06-21 05:25:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e5b19d8e-ce2d-3069-8468-59e229c0b672 | -12.57689 | -58.3776 | 2025-06-21 05:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc74a084-46ad-33ff-8137-3cea555a541c | -21.08442 | -55.77299 | 2025-06-21 05:25:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c21440da-464d-37ba-8858-25738e35519d | -12.57565 | -58.38645 | 2025-06-21 05:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb718276-bbd0-3674-93f2-d1d3e56d5445 | -12.58434 | -56.9909 | 2025-06-21 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c47a4cda-affa-3cdb-8443-a0eba2e8ed2c | -12.47209 | -54.42355 | 2025-06-21 05:25:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 0730e86c-0573-3108-b17a-edbcbb300c38 | -11.87465 | -54.66398 | 2025-06-21 05:25:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 9b635fe9-376f-3711-9149-2b89c4756e38 | -13.24112 | -49.83917 | 2025-06-21 05:25:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d23821e4-4b6a-3b66-a0e7-b186f2baa9c0 | -12.28229 | -57.27011 | 2025-06-21 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 058b2f39-d55f-3b03-bbf3-16a7cf194614 | -13.36607 | -54.2602 | 2025-06-21 05:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2d13f553-2878-31a6-98be-d00c93d5c058 | -4.5429 | -48.0151 | 2025-06-21 05:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 200.9 |
| 1a49b098-a597-33d9-b0ce-963752e61cfb | -11.7791 | -57.2445 | 2025-06-21 05:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 0b5b0812-f8e5-384d-91b9-725b2dc9a135 | -4.5243 | -48.016 | 2025-06-21 05:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 638b9b67-3993-30e8-b28e-2d0baac24c72 | -11.8853 | -54.6722 | 2025-06-21 05:30:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 13057590-3be8-342e-ac48-3b9957036f1c | -11.798 | -57.243 | 2025-06-21 05:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 14cac9f5-5ad3-3d80-be07-bef649b554f6 | -4.543 | -47.9934 | 2025-06-21 05:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 8f9126a3-081c-3e2b-9da9-9f1ded999d47 | -11.8663 | -54.6739 | 2025-06-21 05:30:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| c5366c1e-be9f-3060-bc4e-21392436b468 | -11.7791 | -57.2445 | 2025-06-21 05:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 58872737-8286-3504-8507-c8baec721a24 | -4.5429 | -48.0151 | 2025-06-21 05:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 225.7 |
| bc0ea446-79ff-3f92-9d2a-9d551f5bb54d | -4.543 | -47.9934 | 2025-06-21 05:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 83fe91ee-26df-3f06-8e7a-c1d902253588 | -4.5243 | -48.016 | 2025-06-21 05:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| b840b903-2837-380a-bc8f-ef9b8d3d5330 | -11.798 | -57.243 | 2025-06-21 05:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 83b482dd-1408-36b8-b818-2abdb720902d | -11.8853 | -54.6722 | 2025-06-21 05:40:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 05f99c16-1a9e-31be-a661-34cd0d2e036d | -11.8853 | -54.6722 | 2025-06-21 05:50:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| c238cb81-7763-3d9f-a2b5-c85af6888b7c | -11.8663 | -54.6739 | 2025-06-21 05:50:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 4cba5b70-8fe2-379d-a373-9877f9eddf30 | -10.437 | -47.0594 | 2025-06-21 05:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| f8d3e532-e600-3d3b-8c83-f8e676df52c4 | -11.7791 | -57.2445 | 2025-06-21 05:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 5f584bd6-8966-35c6-b4b1-27ed6ade887e | -10.4374 | -47.037 | 2025-06-21 05:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 4b15becc-0093-3810-a5eb-2d045176a823 | -4.5429 | -48.0151 | 2025-06-21 05:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 199.7 |
| 3ab26223-c14c-310c-89a6-c6465b54d376 | -10.4564 | -47.0347 | 2025-06-21 05:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 800ed4db-b83e-37c0-a849-636f109d5adf | -4.543 | -47.9934 | 2025-06-21 05:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| b5494228-ec91-3b32-ab62-a9edb19245a6 | -10.456 | -47.0571 | 2025-06-21 05:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 04280ae6-f561-3cd2-b5bd-605400861afa | -11.798 | -57.243 | 2025-06-21 05:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 0a49a75f-dfc3-3a3a-998a-30b30fadf849 | -4.5429 | -48.0151 | 2025-06-21 06:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 189.4 |


[Clique aqui para ver as próximas entradas](README28.md)
