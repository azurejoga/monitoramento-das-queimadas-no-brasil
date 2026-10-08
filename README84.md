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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6dbb0648-fa67-31f5-91c9-36d9526ea02e | -3.29067 | -54.00811 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f710de2f-9888-31e9-beae-0a45b2331c98 | -3.76685 | -51.33203 | 2026-10-08 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2be70991-fab4-3a48-8515-7c5d59a366c5 | -3.48516 | -50.08734 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 947e5e47-0ad9-3b3d-85bc-992d803325a2 | -2.93172 | -53.92977 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5f7353c-9534-302a-896c-1b0cb448aabe | -2.93867 | -54.14937 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff60acd1-cdc8-32cf-bb18-9fea95f049a1 | -6.95544 | -51.91881 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 858eef19-7056-33eb-938a-ee4c66d4741b | -2.48431 | -56.11426 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 497a5064-8149-38eb-9877-64535ac3bd89 | -3.10684 | -53.77578 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 82f5ca42-1ad0-3c8d-ac81-245eaeb26b26 | -5.29286 | -60.10284 | 2026-10-08 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ab1a539-b2a3-3844-bc22-4b26746d4dd7 | -3.80943 | -51.53801 | 2026-10-08 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac557d94-4dce-3571-8cb9-c1dd8003088d | -5.75081 | -42.06739 | 2026-10-08 04:46:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a4b1929d-7d44-37dc-ab60-4a280b2a6977 | -5.33529 | -50.98702 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ddfe0915-8c64-3355-a5b2-633ad67fd299 | -8.28943 | -50.27037 | 2026-10-08 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 572a3d3d-ccbd-3286-a35b-ce17650bb15a | -2.58264 | -56.15012 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bada9b97-fa9c-3667-8e0e-01bbccc6a1e7 | -4.57349 | -54.95728 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 5e4d24e9-8713-3937-9425-e3df706e348c | -11.76473 | -44.94792 | 2026-10-08 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| df113e79-9528-3518-9efc-b51ed55dc349 | -3.08209 | -53.95154 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 87350142-9457-372e-b659-a302554932d9 | -3.48178 | -54.62225 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bf5a3393-9ba3-3a22-aff6-0d07c5790cde | -4.12427 | -50.83459 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa3b4758-d5c8-31a9-9f9c-fb03d40e5459 | -2.50947 | -56.25271 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d01f32a5-6db8-322b-b1a1-4bf3868c623a | -3.00995 | -54.12255 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| c89fd646-e1aa-3326-92d6-31c26dbe8d6f | -3.0501 | -53.96413 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e27d067c-38e7-37c5-bf15-f99268f84700 | -2.50847 | -56.23214 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fa03bd9b-46be-34f6-9adb-a2d32f19c32e | -5.00836 | -50.94599 | 2026-10-08 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce1e56df-1cb1-3d75-b4e6-dbd9ed80a7e6 | -2.49625 | -56.14833 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4f38000-77d1-31af-bd76-52b0d2fdb157 | -5.12359 | -47.1102 | 2026-10-08 04:46:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f8053cd4-02aa-348f-86ca-f93669fda63a | -4.83828 | -45.80029 | 2026-10-08 04:46:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84af2dd2-e963-3bb4-b44f-3fc4ca8baed5 | -5.69438 | -53.48817 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2f9ab205-b0c6-300c-a0ad-4e18cda56871 | -6.15805 | -52.65535 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0a2ff26-ea5d-3563-b870-c37068147027 | -5.69727 | -53.49237 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9b4f0817-d39a-373c-9b84-65e0c77acde5 | -3.29692 | -54.03853 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 09075752-f177-3429-bec1-64db05751c26 | -3.05225 | -54.14269 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b3087e1c-7bb0-3ec7-9104-d23b760a5412 | -3.58154 | -54.65457 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2b2b239a-eda9-3ac9-8ee5-3b70450d0971 | -7.20396 | -55.12556 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf6f2a6d-f9fa-36c6-9f9f-553b2f4bd0c5 | -4.96259 | -55.82109 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e4718ac-1766-3bb8-a06f-99f7f92a0294 | -5.0443 | -49.76901 | 2026-10-08 04:46:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4c78fcc-901c-32a7-8d3a-f3616b88aea7 | -5.39861 | -47.94922 | 2026-10-08 04:46:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34cb440c-0836-3603-9330-e4c1ffbf018c | -3.01572 | -54.11 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| e009ea26-6392-3559-b03a-882aafcacf40 | -3.54147 | -54.66234 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 879e446e-481b-37b3-a408-78f852c59a90 | -3.0222 | -54.09304 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| b7f7655e-b290-3c67-969b-1b98713da248 | -3.5664 | -59.4912 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 319b81ea-81bf-3429-ba71-874fc292c2c3 | -3.02242 | -54.18768 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e9db777c-20f1-339d-ae96-1b9b5e614782 | -3.21929 | -53.96185 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1481d3d0-5214-36c7-b064-ff99783e7afa | -3.27295 | -54.07021 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 414c45cd-652e-37b4-9b4d-b047b255de8e | -3.47141 | -50.08874 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f606a03b-15c5-3e29-8fb6-c6ba1ddc07cb | -2.89772 | -56.66801 | 2026-10-08 04:46:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8079a553-ad5e-3b6c-b56b-b59e6f30272b | -3.28692 | -50.43929 | 2026-10-08 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d89d8a5-1f2a-37a7-874e-01297caabdee | -8.08731 | -55.30472 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a25eda3b-a42e-3fcb-a251-8403149ab2e1 | -6.93965 | -46.59157 | 2026-10-08 04:46:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c4cc07bd-92fa-3de1-be3f-ccb02240fc7d | -2.80239 | -54.08385 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9b06945c-0223-387f-b09a-9d23045083aa | -3.11205 | -53.78949 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b0df7a0d-5538-3b7a-89a4-fcab0c879a97 | -6.36027 | -55.15001 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9a511b93-c872-3197-a50b-3aa650aafd2b | -3.47096 | -59.58129 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b45d34b-d8ff-34bc-8481-9977e1f69c11 | -3.00562 | -54.05469 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 5cacc8c8-c5ee-3f41-aa44-65fb789f7ad9 | -4.30799 | -54.79777 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c9027713-a385-3795-a12a-2d535d0c8ddb | -3.29186 | -54.04655 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0a93e7a3-0dfe-357c-afef-2313669a0560 | -4.07433 | -59.84606 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 19bdf019-eeae-3256-aa3a-98eb6467633f | -3.04116 | -53.9495 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 37d1f5e2-34b3-343d-8eae-61f18dc5b77a | -6.22575 | -52.65473 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3004a80-98de-3de7-bad9-1b0cc923d03c | -4.42366 | -59.49435 | 2026-10-08 04:46:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d0ccfaf-d792-3c35-a7a5-982bcf356f60 | -3.71662 | -59.34082 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94c4dc9e-0b17-3f27-82f3-67be843c5b09 | -4.26541 | -46.38888 | 2026-10-08 04:46:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 15202080-19dc-33cb-bdc3-6321175954e9 | -5.75198 | -42.06478 | 2026-10-08 04:46:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| edc49d5c-e513-3094-9ca1-14ef5c745f35 | -3.23107 | -57.87947 | 2026-10-08 04:46:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8708edfe-655b-32ec-9c86-c1ae0728073a | -11.23927 | -45.24493 | 2026-10-08 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 56b4ca88-4dcf-360c-bc7d-f8bf0d7565f3 | -7.34386 | -45.28123 | 2026-10-08 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8cc17a81-8120-39ee-8bdf-cf55cef678b7 | -2.95077 | -54.11341 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e41d791c-9d76-3b8a-852c-71b43a285158 | -3.01828 | -54.07005 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dfc81425-8b9f-3c68-b955-ec502217c89e | -2.78899 | -54.07278 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 76c0effa-fb08-3331-a537-278e23e81b8e | -5.69786 | -53.48868 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b510097f-0d88-3813-b5fa-c7ce7525ba9e | -11.77457 | -43.53611 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20cecd7e-9d61-30c3-9e45-d0b24f681b1b | -7.34121 | -45.28743 | 2026-10-08 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3df50e57-5478-3f52-9ea7-75417331eaf3 | -4.36886 | -54.75557 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df477375-d281-3449-b606-c40846d9b444 | -7.88572 | -54.99661 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c13c826-8e2a-3be6-b53b-28171e733f93 | -4.53853 | -54.98303 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6bd5deb5-a5e6-3788-938d-d2886de2e43b | -8.25514 | -61.39303 | 2026-10-08 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f51fe5e6-f937-38ea-879c-d9f462fc3e92 | -2.82746 | -54.13205 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f5711bdf-d3b8-357b-b389-8ee97c10597a | -7.16779 | -47.78839 | 2026-10-08 04:46:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 70276c97-146c-3b66-b981-d677c96c4d25 | -3.9426 | -56.02073 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a728dca8-5a40-3ffb-a042-55f12ffd9fd6 | -8.71415 | -62.41173 | 2026-10-08 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3058aa2c-be94-3fe0-8432-a601086fbd16 | -4.32248 | -50.78112 | 2026-10-08 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7a774fe6-1776-3029-a2ab-d077611d49cf | -3.99685 | -56.26001 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81193087-3e3b-34f0-a5ef-439715413202 | -4.00579 | -56.25753 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2989c411-83b1-3ade-ad1e-dc116062c66c | -3.43413 | -59.5418 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d2ec5742-5773-3b85-89a0-af4b18dd8e9e | -2.47069 | -56.06416 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0bf031a1-99b0-341d-878e-300ff93f1f0f | -7.22962 | -44.27491 | 2026-10-08 04:46:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9f7e2e3e-6d92-3ba9-b4a8-ad8acb9df830 | -5.34296 | -50.98117 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c2f3eb7-1ed0-3f06-bf81-3b4797be4be5 | -3.31 | -53.86573 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d4787dc4-2bfe-3de3-8c51-a8d97cd3f2bd | -3.96433 | -56.11931 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04b30c02-8802-3a76-b665-c0d7b12a2e23 | -2.58499 | -56.1626 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e8b3f58-5252-3951-a9af-ba570f9d833a | -4.06918 | -59.83537 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 34aa6beb-75b2-3348-b950-63e62da7a5c9 | -3.10335 | -53.7678 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 330164ad-34fd-3b88-8d92-7977880084b8 | -5.6995 | -53.50062 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| ae585366-ef6f-39af-a041-8aa210a1c49e | -4.07271 | -51.09389 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a322f976-451d-38a3-9302-0dd41dea5213 | -7.20751 | -55.10381 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 28332134-89ac-3b50-87cf-1543a3007c84 | -6.22878 | -52.85161 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4aba77a3-e64e-32cd-8da8-ad7760bf17a0 | -8.73585 | -45.1612 | 2026-10-08 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b7fefb95-a019-373d-b184-09c52565a5ba | -3.05694 | -54.22314 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 318d050a-e1d9-3ab4-aeab-dbef4bfcd4cd | -2.50472 | -56.14965 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d51a3619-b064-3a79-b373-c8d99ab107ec | -7.18518 | -52.62053 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README85.md)
