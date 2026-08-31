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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 135f74d1-2e80-3ce5-9fc4-1d716fdca274 | -10.13076 | -45.749 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0bd98c7a-5734-3b45-b97d-237f47b0b649 | -11.37112 | -45.20325 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08df2ab1-7950-3e24-93cd-339698d8c99a | -11.22056 | -45.10002 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 245ebb78-8db1-3319-bbe3-139e334c05da | -11.21167 | -45.33368 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f739acc-615b-3607-8bcb-93b8b9ec02e1 | -6.18359 | -44.93591 | 2026-08-31 04:14:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f437aa9-911d-34c6-94f8-97ea52520aed | -8.37774 | -45.76391 | 2026-08-31 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| be3184ce-b146-334f-bc79-4daea3a45333 | -8.13371 | -45.49551 | 2026-08-31 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 619a397d-7abe-3726-8e3b-22e50f307ba8 | -7.05144 | -45.4016 | 2026-08-31 04:14:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad7c3f6c-e911-31dc-811b-51867691b4af | -11.92746 | -45.06538 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c69cb7d5-50cb-3107-bc81-543d008bf73d | -8.13076 | -45.49065 | 2026-08-31 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 686c0600-80a8-3bcc-b7c6-dc2b149ef8c5 | -7.10562 | -42.76652 | 2026-08-31 04:14:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5fb6b7f5-f754-3381-84ce-662a85d44cfa | -12.39704 | -46.45765 | 2026-08-31 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d76955be-6544-37a0-9d83-08b677e9990d | -12.10454 | -45.03701 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 75db358a-4598-32c6-8046-c144c385c4a5 | -10.99565 | -49.69749 | 2026-08-31 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4b50a99-651f-35ed-803e-928cab33ee11 | -11.34617 | -45.20302 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b37c4907-bcc3-30ff-b07e-cd50fc6ef9ba | -12.39342 | -46.45698 | 2026-08-31 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 10e20a23-401b-3e53-9827-bfa344c1a696 | -7.60573 | -44.92841 | 2026-08-31 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39cbf54f-1b9f-318d-b5b3-20eb50a81d0b | -9.43855 | -45.6753 | 2026-08-31 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6bc0e0a3-189f-3731-a265-edae40a35c33 | -11.3594 | -45.20927 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 81780a72-48b7-3463-a9ff-1f6fbfd7f66c | -7.0413 | -42.19104 | 2026-08-31 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b52f8750-de47-3243-8b91-1fe139d28dbe | -11.37266 | -45.21539 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f5a9bac6-a0aa-347e-8c05-cba3f41162f0 | -11.21999 | -45.32697 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 647998eb-2f70-3bc6-b5df-c7a0bc1c6e9f | -11.36158 | -45.21761 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 323754a8-1fea-335d-bd74-058f04508d4d | -6.84629 | -41.68452 | 2026-08-31 04:14:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 041340b1-9f32-3bd7-bc10-20c8087b68d4 | -11.36854 | -45.21872 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8099e56f-d74e-3fe0-860c-ff1571c428c2 | -5.58944 | -42.32663 | 2026-08-31 04:14:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 8aa4ba53-b693-3c43-ab18-2105212c3c77 | -11.35271 | -45.22793 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 14ae04d6-028b-3c6b-84d4-eba4d5bcf0d9 | -7.60826 | -44.89109 | 2026-08-31 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 98e8638f-6f44-3f59-8e26-81e2af04c2a9 | -9.80153 | -46.44153 | 2026-08-31 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a58983f7-56f2-30c7-9e96-72c07c84dd3a | -11.62878 | -46.73248 | 2026-08-31 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5636d55-72db-3723-998c-c7cc3ee1e7b0 | -10.54549 | -46.20509 | 2026-08-31 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d7d6236-0a39-3030-9e8a-fe7760081185 | -11.49412 | -50.33251 | 2026-08-31 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b94c07af-192f-3a8a-9157-8c893c720b30 | -10.85483 | -50.48891 | 2026-08-31 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fffc33c0-7c3e-32fb-b6dd-d8b34137552e | -7.11768 | -42.84071 | 2026-08-31 04:14:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5fcea75c-c1f5-3f50-99ac-6bd161a9b294 | -11.93152 | -45.06219 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 734b5fa7-2dbb-38f3-9847-242513157f87 | -7.41508 | -44.25852 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17bf03ac-f1c7-3fcf-b1ef-55f01bbfe890 | -11.93335 | -45.05117 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a37ec5c7-22e0-301c-af7f-b65cb2bf2951 | -7.10256 | -42.23281 | 2026-08-31 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 996c1f98-143d-3a35-8b27-bbd1e14c8004 | -4.39396 | -47.83541 | 2026-08-31 04:14:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d02f226-77e5-396e-9fb2-6130793ec73c | -7.63773 | -46.72505 | 2026-08-31 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eed6ba7e-a3a1-3618-8a0e-7be0cdd5a532 | -7.93455 | -44.2544 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4ce9b068-7d07-381c-ad17-4466fcd790ba | -11.354 | -45.22021 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 40e49c8b-172b-3866-a11e-f49e23740b60 | -7.98666 | -46.51906 | 2026-08-31 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ae26e82-d251-3d7f-885d-4f114370eab2 | -10.40065 | -45.08564 | 2026-08-31 04:14:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6a4ff9a-864b-3666-b9b8-3e44628d3029 | -9.66952 | -47.93728 | 2026-08-31 04:14:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12ca4f60-16a9-3d4e-898e-8428c8622d8f | -8.14927 | -45.46952 | 2026-08-31 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4672c20-507b-3328-9441-5672d4cc439b | -7.60911 | -55.29105 | 2026-08-31 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cbe00b06-bae2-304d-ad43-bbe3e693425f | -11.35875 | -45.21315 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8b5aca47-871d-350f-87fa-e3b4a2b8ec84 | -11.37346 | -45.16785 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e310b0b0-64f6-3c61-aabe-d8dd0eabce6c | -11.22873 | -45.09362 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5b17e095-2198-3cfe-9cbc-24ef89f34e8d | -12.09738 | -45.05917 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 12422e0c-a204-3994-a281-2fd06be3d60d | -11.32798 | -45.17267 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 886e17b9-0bcf-3f03-b8f5-647fa72a9470 | -11.92808 | -45.06163 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 930cbbc5-b10d-3c9a-88ef-6cdb6a5bfa4d | -7.28096 | -49.83837 | 2026-08-31 04:14:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4d03c1bf-dd98-3d92-b44c-9df13f70a69a | -6.17996 | -44.93532 | 2026-08-31 04:14:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aff03c0c-338d-311f-9db2-856dfd33cdf0 | -10.81386 | -45.34652 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f6b2bf6-4105-3f81-9428-08f283799a60 | -11.67535 | -47.61359 | 2026-08-31 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8a01b499-38a8-3f9b-87b4-61cd6c760616 | -11.20416 | -43.37709 | 2026-08-31 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 013725b5-206c-39ec-aaac-a3fad633ff2f | -11.21646 | -45.10331 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a43ff525-bc4d-34ac-8e62-9be4ada62410 | -10.79727 | -50.50526 | 2026-08-31 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7fbebb27-f811-35e5-b622-510412c41022 | -10.12714 | -45.74849 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4d3ed720-f18a-315d-8ea0-2fe053bc5d40 | -11.83218 | -46.76242 | 2026-08-31 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 36d59ea1-69de-3794-8216-b906f371a855 | -9.97337 | -46.82957 | 2026-08-31 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78037d68-d45b-3757-b06a-bdc9b0e0cfa7 | -11.93213 | -45.05853 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 47073278-904b-3cfd-9000-2041ada49b87 | -10.73369 | -44.88254 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5fd9c9e3-fd44-34ef-95e3-ef009e398a54 | -10.06032 | -48.6656 | 2026-08-31 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2c15d62-9c75-3d4a-ac4a-e5d172ce98e5 | -7.97389 | -44.29594 | 2026-08-31 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e291295a-74b1-3a2d-9e50-576ce38c3feb | -11.34488 | -45.21068 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 37.6 |
| bd6c0843-e4aa-30a6-b2a6-4f7e5b45e0b6 | -7.18516 | -43.70886 | 2026-08-31 04:14:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2684d4a-6f69-365a-a295-7c692be0ab5e | -10.73291 | -47.96932 | 2026-08-31 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b14f22ca-bb81-3ed9-925d-dbaa8529449c | -7.1473 | -46.1671 | 2026-08-31 04:14:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2f8749e-cdec-3a50-bd30-57adf05ac4f0 | -10.84066 | -45.35907 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 828c14d1-d55f-3c12-a428-327e271fd7a9 | -7.41572 | -44.2546 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05f98c73-93c4-38b0-8b26-ffe7f969cffa | -10.82308 | -45.3562 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d69b43c1-5624-3b4a-991a-8622cb1034c0 | -7.97735 | -44.29651 | 2026-08-31 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1bdaf9fb-4f96-3c96-874b-e2df9fd9356e | -10.79768 | -50.65674 | 2026-08-31 04:14:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| eeff9ebf-54cb-3805-9263-b4262d8d1c1e | -7.10669 | -42.78112 | 2026-08-31 04:14:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c5c925fa-e2e6-3496-a7ce-bdbd6f4372af | -11.3657 | -45.2143 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 857d669a-a731-322b-b904-091b994a2461 | -11.37047 | -45.20711 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 143b746a-b6e4-395c-976c-cf75584b9c9c | -7.64082 | -46.73079 | 2026-08-31 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4d2678d-4ad1-33ad-a173-3911a5e2f04a | -11.26155 | -45.05811 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| abed769f-c1ec-3b48-b285-6ab45f905533 | -7.41791 | -44.26301 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94168d3d-35ab-3854-bce5-d664aed9342e | -7.04075 | -42.1945 | 2026-08-31 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 578849e4-837a-3a6d-bf08-acd5863f6be1 | -11.49972 | -50.32837 | 2026-08-31 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9dd894e-9252-32f9-ab2e-03806a758cdf | -8.38065 | -45.00066 | 2026-08-31 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c1b3aa7c-a10e-3a8e-aa08-52d2c1db2596 | -7.93241 | -44.28902 | 2026-08-31 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6bb724dd-3c84-3774-bc4f-dd9fb7c6312d | -8.61052 | -54.77817 | 2026-08-31 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f49ceea5-79fb-3920-a8ca-1b1e9637c821 | -10.05173 | -48.6893 | 2026-08-31 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c0ed016-3e18-3629-bb2c-1a0a70ade95d | -8.7559 | -45.38337 | 2026-08-31 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 68b2ce1d-9a39-3c5c-86e0-3fed8983c038 | -7.06503 | -42.21259 | 2026-08-31 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9b0a9dee-bb3a-3761-bbc0-fdd0e175fdca | -7.28365 | -44.52937 | 2026-08-31 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b26b4cc-988a-39ee-87aa-e056ca764013 | -10.74377 | -54.04652 | 2026-08-31 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f99a9ab-b41c-3fcc-b965-153479c155ba | -8.38975 | -44.98966 | 2026-08-31 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15b4712e-11eb-3571-a03c-ac1d6bde95e4 | -6.92247 | -55.72376 | 2026-08-31 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ca02629c-e323-33e0-8d15-f6ac8cd66ef1 | -11.36265 | -45.18989 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 430d54ae-5a8b-3ea9-8315-31d4265d6847 | -8.61209 | -54.77777 | 2026-08-31 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff67b72b-f9a9-3591-8f59-945f34ffc2ba | -14.22661 | -52.85188 | 2026-08-31 04:17:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 505e469b-9da0-33dc-8918-d7d6dc904bc4 | -14.19994 | -44.58598 | 2026-08-31 04:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e609db61-7068-3953-850e-84179d200a55 | -14.57763 | -54.12383 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7c1a97fd-983c-37cf-8d91-7e7ac0134ca6 | -12.95068 | -45.94832 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README32.md)
