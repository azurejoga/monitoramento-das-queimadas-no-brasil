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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b177042-f524-3913-ab6f-31a7d7016b24 | -17.5076 | -39.94521 | 2025-07-23 04:36:00 | NOAA-21 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 473797ff-e826-3f28-be72-071a066d3a90 | -16.0903 | -45.17203 | 2025-07-23 04:36:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66c1bdfd-aab9-3892-8164-bad5b63fd876 | -16.40228 | -46.87629 | 2025-07-23 04:36:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 24d4100d-e0e2-3a93-9da2-581769967c40 | -18.6612 | -55.72545 | 2025-07-23 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 11d76c6b-8803-359a-a0a7-ced92058397b | -17.57082 | -47.50969 | 2025-07-23 04:36:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 750e6f96-eabb-3b41-9d6d-edb2403b5f2e | -16.04427 | -43.72498 | 2025-07-23 04:36:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dddb613f-75cd-3a14-b0c9-b77118960f49 | -18.52666 | -48.25286 | 2025-07-23 04:36:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 200105af-4fe2-3572-b570-8b734a92f255 | -17.91359 | -47.7632 | 2025-07-23 04:36:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b7519b4-6af9-3e5d-94f8-bebeedabf5cc | -16.40289 | -46.87184 | 2025-07-23 04:36:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2cce7c44-2cfa-399a-a7ec-e948512e4314 | -12.35532 | -63.41599 | 2025-07-23 04:36:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 47128e7e-2e9e-350c-92a8-0471bd9d405c | -16.09785 | -42.2787 | 2025-07-23 04:36:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 0fe7b77e-9c1c-34e4-94ed-6ceda4459f3c | -17.78351 | -52.43449 | 2025-07-23 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e994a951-ef28-3dbb-a80e-2ff771e24a35 | -19.12723 | -46.56201 | 2025-07-23 04:36:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9021c0c0-8bc8-394f-a9a8-74374de78ced | -13.72425 | -52.00778 | 2025-07-23 04:36:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 58c9ba38-4c07-3523-999b-02ae9bd2e513 | -14.74683 | -46.30268 | 2025-07-23 04:36:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9425efe4-b8d8-3d38-af61-2676d78db329 | -12.35059 | -63.42654 | 2025-07-23 04:36:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 6ad6f655-e8aa-3beb-9a48-e15066198592 | -14.77342 | -48.2685 | 2025-07-23 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1a8cabdb-20ba-35b5-acf8-35ade0718720 | -12.35388 | -63.42286 | 2025-07-23 04:36:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 43ba4377-7d8d-3849-9466-46291d4086a1 | -22.37791 | -42.53896 | 2025-07-23 04:38:00 | NOAA-21 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 39532805-84db-33b6-9324-cbb84e263d19 | -21.43744 | -53.32191 | 2025-07-23 04:38:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 20f9fd18-206b-35f0-b58a-28516ad14ea6 | -23.37813 | -53.61983 | 2025-07-23 04:38:00 | NOAA-21 | ICARAÍMA | PARANÁ | Brasil | 4109906 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b5f02a7c-b24a-36e1-867e-0835a211509f | -23.25438 | -52.1936 | 2025-07-23 04:38:00 | NOAA-21 | NOVA ESPERANÇA | PARANÁ | Brasil | 4116901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 100aab4b-81e8-3fd8-b62e-5351bb9a25db | -22.84493 | -49.17278 | 2025-07-23 04:38:00 | NOAA-21 | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9a3f4da3-f41e-3d5d-b881-50a7b0b8203e | -23.59376 | -54.32696 | 2025-07-23 04:38:00 | NOAA-21 | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| be16bc99-766b-3c7b-af9f-48b593ba3640 | -26.86377 | -51.41565 | 2025-07-23 04:38:00 | NOAA-21 | SALTO VELOSO | SANTA CATARINA | Brasil | 4215406 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4767d09d-aab6-3d7d-b79d-e43ddb5ec451 | -22.80269 | -52.48991 | 2025-07-23 04:38:00 | NOAA-21 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9db7e763-9f7e-37a9-a948-22c9f016594f | -23.25379 | -52.19735 | 2025-07-23 04:38:00 | NOAA-21 | NOVA ESPERANÇA | PARANÁ | Brasil | 4116901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5792161d-4d8a-36f6-85c2-7a541d3c6942 | -22.39713 | -49.79102 | 2025-07-23 04:38:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d20dcb59-6bbf-375a-9c5e-386d0d26b141 | -25.54065 | -49.39993 | 2025-07-23 04:38:00 | NOAA-21 | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c788edf7-4e50-3d7e-9549-ad5ff4f52641 | -23.00711 | -48.62105 | 2025-07-23 04:38:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79446f63-5b56-3300-a3f8-9363fd48f499 | -23.21962 | -46.6425 | 2025-07-23 04:38:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 2ac93642-2cc0-358b-b74b-2cf4a39395ee | -20.28487 | -55.493 | 2025-07-23 04:38:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad590aa0-167c-34c6-895e-b18374a9d74c | -23.30684 | -46.84573 | 2025-07-23 04:38:00 | NOAA-21 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c3078d04-6c83-3a00-87d2-c25b5af35d0e | -25.09966 | -49.50916 | 2025-07-23 04:38:00 | NOAA-21 | ITAPERUÇU | PARANÁ | Brasil | 4111258 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 2ebb4a02-5954-3df8-a3bb-42f717986d3d | -25.01693 | -53.27961 | 2025-07-23 04:38:00 | NOAA-21 | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 61c70fe3-8a8f-3546-8ae2-ec3019727851 | -20.47692 | -53.6758 | 2025-07-23 04:38:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14543606-e9b3-3a8a-811e-580abb0d87e8 | -23.56268 | -46.60693 | 2025-07-23 04:38:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 25b32879-1c0b-394d-95d6-2a97276791cc | -20.49486 | -54.69897 | 2025-07-23 04:38:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c1122610-5871-37c3-b8a9-15e75dc19134 | -21.32591 | -48.62599 | 2025-07-23 04:38:00 | NOAA-21 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 196014fd-0f72-39aa-9398-16fdee339290 | -21.44135 | -54.57869 | 2025-07-23 04:38:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a7dfc7b2-66cf-3a1e-a302-378035c02c2d | -20.2895 | -55.48896 | 2025-07-23 04:38:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe79f56c-9db9-3713-b1be-3726d13de7e6 | -27.08719 | -48.63729 | 2025-07-23 04:38:00 | NOAA-21 | ITAPEMA | SANTA CATARINA | Brasil | 4208302 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2ee94f51-b32e-3751-8232-a4dbf3e33c2b | -22.15546 | -52.68113 | 2025-07-23 04:38:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f7660a54-9573-3e88-ae26-f483f031f09d | -20.29834 | -54.07885 | 2025-07-23 04:38:00 | NOAA-21 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3c6dc8a1-5c0c-3784-81c9-0d361ea35347 | -22.15818 | -52.68551 | 2025-07-23 04:38:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 34b24486-0054-32c7-bfac-19ee93842e6e | -19.79217 | -55.34909 | 2025-07-23 04:38:00 | NOAA-21 | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| edf855a0-1f4f-3745-8196-e3f4a49260df | -22.16091 | -52.68988 | 2025-07-23 04:38:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 97e965c3-3304-3104-a0cf-5db0072ac996 | -21.38792 | -48.67478 | 2025-07-23 04:38:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 991492a6-dc6c-326f-b872-832d78b9406c | -22.05908 | -47.91184 | 2025-07-23 04:38:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 183dac78-fea0-3670-b908-fd32277bbbcf | -21.32268 | -48.6265 | 2025-07-23 04:38:00 | NOAA-21 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7b4f67c0-64dd-3c4b-91ed-8b42f5ff1268 | -21.44489 | -54.5794 | 2025-07-23 04:38:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e2096dea-cc5d-307c-ae6b-84ec93be1cb2 | -21.44209 | -54.5744 | 2025-07-23 04:38:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8e4d17ce-f558-3ecd-b617-f9892ba2f3f8 | -22.15485 | -52.6849 | 2025-07-23 04:38:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fdcc2b9a-9b32-3f00-992a-aba9927b34a4 | -20.56172 | -54.6576 | 2025-07-23 04:38:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1e17ebb-3c9b-367d-94ee-546965e95012 | -23.05788 | -49.69169 | 2025-07-23 04:38:00 | NOAA-21 | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| a9327374-e9db-36ab-99ba-662c88ee44c9 | -21.91138 | -47.39954 | 2025-07-23 04:38:00 | NOAA-21 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 74e5b24d-e277-34c5-8af9-ac5892a0a1a8 | -22.84434 | -49.17701 | 2025-07-23 04:38:00 | NOAA-21 | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3ac434d3-985a-3eb7-8258-76526c0e2115 | -21.37198 | -48.60699 | 2025-07-23 04:38:00 | NOAA-21 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0b6b75c9-9b49-30a1-97c0-9b54037358e5 | -20.29482 | -54.07817 | 2025-07-23 04:38:00 | NOAA-21 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ccb2cfc6-1f82-3df2-b6ce-8d3e2ffffe1f | -22.40055 | -49.79158 | 2025-07-23 04:38:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1146e6d8-9420-37c3-b976-e730d30fccaa | -20.64521 | -56.54847 | 2025-07-23 04:38:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f00910d7-b2fc-3bb2-a176-a5e76af23e23 | -23.3986 | -47.01047 | 2025-07-23 04:38:00 | NOAA-21 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e2eccb68-83ae-3aa0-a46b-e39c504f046d | -23.25497 | -52.18985 | 2025-07-23 04:38:00 | NOAA-21 | NOVA ESPERANÇA | PARANÁ | Brasil | 4116901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0f7d58e9-0695-3a7c-a77f-87a2c651654e | -22.24518 | -49.58375 | 2025-07-23 04:38:00 | NOAA-21 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| db3d4146-9bc3-31a4-873c-82bc62dc0e88 | -22.77182 | -46.98613 | 2025-07-23 04:38:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 72795d42-8c9b-39a3-8cbe-be65396c4329 | -23.3115 | -46.84064 | 2025-07-23 04:38:00 | NOAA-21 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c42b6e60-1ea7-31a1-971e-17f8c5db522f | -27.79749 | -50.38141 | 2025-07-23 04:38:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 30bd2925-eb71-351b-a1f9-de72ce36c3e8 | -21.36843 | -48.60643 | 2025-07-23 04:38:00 | NOAA-21 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 70e1b2ac-5d81-3a2d-aa7a-c3e265688d71 | -22.39998 | -49.79559 | 2025-07-23 04:38:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 66ca8ca9-6c90-324b-9037-59bf2a27d858 | -20.64437 | -56.55302 | 2025-07-23 04:38:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fd882029-bf31-34c9-8645-391a5c7faebf | -22.91453 | -53.14584 | 2025-07-23 04:38:00 | NOAA-21 | LOANDA | PARANÁ | Brasil | 4113502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8c8ea155-f895-3362-952a-98bdadbb0dc4 | -22.58348 | -48.30716 | 2025-07-23 04:38:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cbcdf5dd-ec87-3b92-b317-6dc46cafdf9e | -23.30198 | -46.95281 | 2025-07-23 04:38:00 | NOAA-21 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 1d149644-2626-31ac-880a-59feda0efb16 | -21.44563 | -54.57511 | 2025-07-23 04:38:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b7d6b21a-efbc-3aa4-94db-ead78d817bb4 | -25.10004 | -49.51054 | 2025-07-23 04:38:00 | NOAA-21 | ITAPERUÇU | PARANÁ | Brasil | 4111258 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 7a0ae894-cbf2-317a-bd28-937935a21250 | -23.55739 | -51.28509 | 2025-07-23 04:38:00 | NOAA-21 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8d2846ad-2d00-3cc5-8866-5450d44448e0 | -24.95583 | -49.63971 | 2025-07-23 04:38:00 | NOAA-21 | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| c8298676-500d-3d00-9acb-320a96eab09a | -25.03814 | -51.93564 | 2025-07-23 04:38:00 | NOAA-21 | GOIOXIM | PARANÁ | Brasil | 4108650 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 460775b6-5591-3bce-a326-fc8c5ad2a7c3 | -23.21062 | -50.28569 | 2025-07-23 04:38:00 | NOAA-21 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1b7237b6-0587-3ab0-a930-91085cdc66f9 | -22.80329 | -52.48616 | 2025-07-23 04:38:00 | NOAA-21 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b1977550-9faf-31a7-b213-f1a0252cfc45 | -22.89086 | -45.17812 | 2025-07-23 04:38:00 | NOAA-21 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7c729f65-0aaa-30b6-a154-0b28c61e1af5 | -3.1833 | -49.4429 | 2025-07-23 04:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| f9faa0e8-8c18-3ea6-9a4f-0a40986799f4 | -3.1649 | -49.4435 | 2025-07-23 04:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 243b1239-518e-314a-86d0-cab1e532a264 | -3.1648 | -49.4648 | 2025-07-23 04:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 4ef46a1c-226c-3a8b-ab75-fcf4ef887c6c | -6.5631 | -51.1126 | 2025-07-23 04:40:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 902a5899-f4a2-36eb-98cb-680dd65725e6 | -3.1832 | -49.4642 | 2025-07-23 04:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 5be30a33-658c-33ae-aa1c-2dc8cb97cfe2 | -28.93311 | -55.0835 | 2025-07-23 04:40:00 | NOAA-21 | ITACURUBI | RIO GRANDE DO SUL | Brasil | 4310553 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 0a888b1a-e6a7-3749-a17d-7ed86f140ebd | -3.1833 | -49.4429 | 2025-07-23 04:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 231c0254-57c4-375d-b42c-d3b5b3c66c77 | -3.1832 | -49.4642 | 2025-07-23 04:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| c72bda69-89b7-3bac-a9ae-dd3323416be8 | -3.1648 | -49.4648 | 2025-07-23 04:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 4408cbf3-f40e-3a54-b46c-5f1491d4b438 | -3.1649 | -49.4435 | 2025-07-23 04:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| b906462d-7e05-36ec-b6ad-524bf7ccb6a5 | -3.17646 | -49.46056 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 1c9e9b67-05cb-3b5e-8cbf-f98a714e1a07 | -3.16648 | -49.44971 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bc5cf76f-533a-3afe-a475-fc5d44a17718 | -3.16578 | -49.4543 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e967d32c-71a3-32ba-ab9b-425ad3142333 | -5.67729 | -43.66485 | 2025-07-23 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b73bbc85-a681-3bc2-94fc-6a9f1cce20d3 | -0.75007 | -47.75529 | 2025-07-23 04:57:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86b461a9-39cd-379a-ae6f-786298f47e49 | -3.17027 | -49.45029 | 2025-07-23 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 230a4e76-cfa2-35d0-b4c1-58d3f3b311f9 | -5.68769 | -43.675 | 2025-07-23 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ed2a5a83-add8-366e-902d-4fa86c047aeb | -3.27291 | -53.02055 | 2025-07-23 04:57:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 605184e2-2685-3760-b18a-25ba17785e5c | -5.688 | -43.67329 | 2025-07-23 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README14.md)
