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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc7e2bc5-d82c-3861-9c09-2e4bed588c8b | -3.11976 | -53.7648 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d45aa279-4af6-3881-b44b-378eeb0b5024 | -2.50295 | -56.13334 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c183a2e-1484-3fb2-ac5b-82457827966a | -2.87584 | -54.47725 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29f7cf7b-2b52-3cfc-95cc-09b28de0f2eb | -2.94117 | -54.10915 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 62b0547a-901e-3736-9709-6b69127edc20 | -8.21736 | -46.32051 | 2026-10-08 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9b039f74-7182-37f3-b39f-31c3f16602a0 | -4.3594 | -59.94451 | 2026-10-08 04:46:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6b11373-f7db-3439-b56c-efaf374bd49b | -3.84843 | -55.9833 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 76e6e4b3-ddec-3a5c-af25-68b357c43d25 | -2.89951 | -54.15681 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b5d5121-9748-3d96-9bde-41cd2ebf0a66 | -3.08718 | -54.29631 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 48c0b819-98be-306f-92b1-159ddfcc1923 | -3.00583 | -54.07706 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bd7ec087-c0bc-39f7-b260-4518eabbb5ee | -11.22236 | -45.26723 | 2026-10-08 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 92be9f99-e46b-3aa3-b926-a40bb1ba0832 | -2.9583 | -54.13717 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 509d7dfd-9c8f-34c3-a70d-57492ae1b35f | -10.30722 | -46.61853 | 2026-10-08 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b27fc67-4823-36f9-8443-ad1634083704 | -7.89381 | -54.72036 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d66ea8d-42cc-34c3-be3e-87b96bd1e304 | -2.95845 | -54.15973 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 29cd3b7e-9e3f-301a-be92-bf196ed9a6db | -2.87388 | -54.19825 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8f2dbd18-cb1f-31f7-a45d-a94cec7dd476 | -11.00155 | -45.42039 | 2026-10-08 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c6f8ab2-3e54-3fdf-96b1-0634ff5148ec | -3.05851 | -53.93458 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c0f34cd-d7fd-3041-9cd0-42ef45d2ef6b | -3.4761 | -59.57936 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8039732b-9b48-3fce-817d-2cd876bf044d | -11.63103 | -43.68949 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 26215912-120f-36e7-b836-38b70ffeee84 | -2.90193 | -54.02242 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 66b483e7-1bc2-34e7-be0f-454809e43641 | -11.11069 | -45.68588 | 2026-10-08 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d559fff7-388e-3fff-9000-b4d5b55f0e7b | -5.96531 | -55.38166 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 425ce218-4401-3936-bb53-93157ec51572 | -7.41012 | -55.57452 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2631afb4-7559-3ace-8576-3d57cdf2fc0d | -4.28897 | -50.77945 | 2026-10-08 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d7a1776e-742d-36f6-8b2e-81a22be8c666 | -2.84421 | -57.4845 | 2026-10-08 04:46:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 592038d2-6d6e-3ff9-8c8f-3214b61e4616 | -6.86726 | -59.34902 | 2026-10-08 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4d26b396-ef3b-3ebe-8228-40c572b14f33 | -3.5286 | -54.646 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4934b569-956f-350c-acb5-940e87d681dd | -3.00625 | -54.12197 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| d23ed3f0-be7e-3915-a5e9-a2fac5421c6a | -4.96178 | -55.12374 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1584b774-d122-36e0-b73a-56dae02c4e27 | -3.05513 | -53.95606 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 72cfdfe2-63cf-3614-90da-0d8822d7a974 | -2.7786 | -54.06665 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 19113a2f-4de1-3d15-beec-bd146c37f6e1 | -3.11065 | -54.17273 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 94c0203f-6b35-345d-a0dd-8cc4f3d1f5f0 | -2.99037 | -54.07915 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 3c6bb60d-94de-3c89-ae4d-f9398010f4fa | -11.23764 | -46.24767 | 2026-10-08 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b368b08-88be-3c32-a355-baf37477088e | -10.7707 | -46.54163 | 2026-10-08 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d06699a4-0902-3030-a24d-96f4e1ede7f9 | -3.43651 | -59.62613 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5bab9ad1-43ab-3208-82c1-b5518acb0abf | -3.78473 | -50.75998 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05b7497f-522c-3c2f-a53f-847c54e9fd40 | -2.47006 | -56.06808 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b68b4a17-2aca-3be6-b399-04d054808c2f | -7.46194 | -42.85451 | 2026-10-08 04:46:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d95f06d2-84d2-37a0-91fd-1707056a64a3 | -6.99941 | -59.11465 | 2026-10-08 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a5741e6d-f067-3b5a-970d-e269e2cd5165 | -3.2596 | -54.03857 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 0c1661c6-3d79-379e-be11-708fdd0a70b2 | -4.63542 | -48.8571 | 2026-10-08 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79f83701-5aac-3f98-9d41-4e3008dca636 | -6.31692 | -43.34892 | 2026-10-08 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| e3324329-c8ba-315b-8b52-1bc30969bb4c | -3.08789 | -54.29184 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f052b9ec-9fe1-32e3-a430-a0cc0eaa12cb | -3.01112 | -54.09132 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| cdccf273-c24c-3d17-9495-160c61441752 | -8.72259 | -45.19088 | 2026-10-08 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2fdb64c0-7d36-38b9-b195-dfe46420cf9f | -2.79059 | -54.08652 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 36c4c057-2ea5-35d9-8f11-51a234e60964 | -3.70199 | -54.22527 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6486d375-fe9f-3091-899f-27d9303e52ee | -5.74217 | -53.45655 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 044d7a73-d669-3629-87ab-9790fad9814d | -3.28226 | -54.03621 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31f1573f-904f-3b3b-becd-1ed3cd79884b | -3.74058 | -59.45098 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf1de323-22ed-3f83-a619-281dc04202d4 | -3.03488 | -54.10853 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e49641a1-dcda-3ad2-b827-30f53de50ac4 | -2.78619 | -54.09035 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 122b3033-365e-3922-83ab-f1d40e19edac | -3.10423 | -54.28524 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 769d1232-8aae-3cce-8efa-40e6a7abf15c | -3.2971 | -54.06064 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 87bf3056-b78c-3178-802c-162597638dc2 | -3.10352 | -54.28971 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9d83b790-9478-311d-92ba-2074c2fac886 | -9.64873 | -54.47492 | 2026-10-08 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 098ed453-7330-3028-ac04-862e79ba4839 | -3.06679 | -54.25668 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1039dd55-a1a8-3db8-93a9-ca3adbf1821f | -6.9813 | -45.1366 | 2026-10-08 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e73938e6-8b8b-3b60-bc9f-795198ca1530 | -11.6291 | -43.70446 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 99f9bec6-d4f5-357a-9419-2cd1c1cfd5ad | -7.19206 | -55.12856 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6e697751-129f-3ba2-8e75-c85f17ca05cb | -3.282 | -54.01555 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4f544966-14dd-356a-a5ed-69c4568861b2 | -3.31456 | -54.04567 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| cae3ea06-57b4-3761-b2f8-f198b27ff9d5 | -10.97682 | -45.39719 | 2026-10-08 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 367e2235-19aa-393e-9e6b-dd7acf9ebb95 | -7.46641 | -42.82077 | 2026-10-08 04:46:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 256a69d7-a832-3f9a-8f15-7b43f6b6e2b5 | -2.97754 | -54.04145 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 82b2c535-4fb1-3894-bff5-4a6f01677e4a | -3.28191 | -54.06416 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6494b281-2f49-398a-99dc-5c02a4664f21 | -3.11435 | -54.17333 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 74d7f7d7-ce44-3944-9fc3-956faa9e023c | -9.09302 | -61.13472 | 2026-10-08 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf47c4e3-ac19-3f23-9988-61b458076496 | -3.02353 | -53.9424 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 953c79c0-0f3b-3951-816a-45d0d60ea964 | -6.85013 | -41.76523 | 2026-10-08 04:46:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 8bd1f1e9-0efa-359b-af9b-c9570a46404c | -2.5036 | -56.1822 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 53ce92fa-1a90-30e1-920f-98d0cb5af956 | -3.20169 | -53.95481 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 43f4b0cf-20f5-33ec-a317-56f8e35c40ad | -6.05535 | -44.02988 | 2026-10-08 04:46:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e8042638-c710-3927-8f71-3a3b00e3a6e7 | -6.11504 | -55.69898 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 03b1533f-f299-382e-bb40-01b4a26aaaee | -10.47027 | -47.24104 | 2026-10-08 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43863cee-b16e-358c-815a-62163e5aea2a | -2.93221 | -54.16644 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 73c66084-821a-35b1-bc6c-ff61f5891331 | -3.09677 | -53.71524 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8a8223c5-d0f5-30d0-a968-15e6654be0a0 | -6.65223 | -47.90844 | 2026-10-08 04:46:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ce3f0bcf-8d1b-3f31-9732-8a9761a6916c | -3.28764 | -54.07253 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e429066-9180-3c50-93f2-99a7c21e167b | -10.42268 | -47.26202 | 2026-10-08 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 36b28fa1-db5a-3593-bfb1-354e9d5479e3 | -3.29029 | -54.03307 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0ca5ffb2-239b-3110-8c3c-dab1214c664f | -3.70291 | -61.32735 | 2026-10-08 04:46:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b2a9c0d9-5c3a-33ee-8529-2b43284123a8 | -5.67543 | -46.35194 | 2026-10-08 04:46:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f252af05-794b-37b6-9b73-b89e6366a609 | -11.63982 | -43.70256 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7541ce92-1392-3b2f-ace8-d215abab26a7 | -5.96608 | -55.37693 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d12f84fc-60ce-33f4-9336-d7f59549e108 | -3.67585 | -54.50378 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0b8edba2-4a7f-3696-a5dd-d5d9975bec90 | -6.11177 | -55.71882 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1f26b84c-bbab-318d-9c69-05a1a34396f7 | -4.36399 | -55.64411 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 39cbad1a-ab13-3373-9f56-cde058179b77 | -2.84443 | -54.12113 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| cf4c24da-6f57-348a-83df-152aa250f2b7 | -3.54245 | -55.52669 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 92dd15e7-9875-38c5-9325-d7dbf55e6fea | -3.28529 | -54.04254 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c967e7ec-11ff-3ff2-a02f-6b7dcd07e32e | -3.17812 | -54.74546 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| be40f4be-53ae-3bec-9ff9-f4f8f981035b | -6.05708 | -59.92923 | 2026-10-08 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15de2914-6f27-3075-a7bb-ffa46c1d2215 | -4.9294 | -55.86116 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2864596b-fcbd-3ee6-bbe3-4d8af0dd623e | -3.04952 | -54.38793 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 969e31ea-3d93-34eb-bbb3-cc6594637a6a | -5.24765 | -50.91634 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb2dd0ba-c1fe-347d-a5f0-4925668b4bfd | -5.68742 | -53.48711 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c526c443-d610-3b45-be27-cf6449318d4c | -11.39156 | -47.55484 | 2026-10-08 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README91.md)
