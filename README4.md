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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c1f238b-98ed-3594-b8df-0bcff31c081b | -17.3472 | -46.84312 | 2025-10-07 00:11:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 54463ea9-6e3b-3944-89a8-6f8ee6d553d1 | -14.1616 | -44.76159 | 2025-10-07 00:11:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 66c3045e-5d50-32b1-b7b7-dab1bc1c846a | -11.94974 | -45.49738 | 2025-10-07 00:11:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| baef7854-e295-399b-8393-785ca4bb9e2e | -16.28573 | -50.99326 | 2025-10-07 00:11:00 | TERRA_M-M | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 161b405d-ab30-38ea-b669-90f73eed6da8 | -12.16743 | -50.92209 | 2025-10-07 00:11:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 23.6 |
| d12085d3-d23c-3232-b2e5-74978d8cecf2 | -17.95573 | -44.40364 | 2025-10-07 00:11:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 879d6a93-3803-348c-9508-1b06a671882d | -16.62069 | -42.45008 | 2025-10-07 00:11:00 | TERRA_M-M | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3544e183-0adf-3281-b3b4-4d2e880fc2fb | -13.23086 | -47.80846 | 2025-10-07 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 13379b99-fdcc-3ec6-8b88-1f287bf9f9dd | -12.34909 | -44.21654 | 2025-10-07 00:11:00 | TERRA_M-M | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| da0da403-b71d-3158-844c-349b0a8a2e9e | -14.91013 | -46.85891 | 2025-10-07 00:11:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| f41c2041-2148-3bb8-ad55-99782c042856 | -11.72004 | -45.43841 | 2025-10-07 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| bb346c60-8f18-3d78-a1d2-f8cf85130438 | -11.84467 | -45.05669 | 2025-10-07 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1754eb31-276d-390f-8b22-85704f17a150 | -11.78112 | -45.13065 | 2025-10-07 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 226d4d83-f338-3b19-8abd-9b480aea9558 | -14.29351 | -47.41802 | 2025-10-07 00:11:00 | TERRA_M-M | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c1d93fa1-01a4-3183-8b7e-99a6c9c215a2 | -12.43402 | -45.61048 | 2025-10-07 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 35021f66-ae32-396c-b9f6-55a0237ad0d4 | -15.96803 | -50.8417 | 2025-10-07 00:11:00 | TERRA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 32.1 |
| c8623dcc-fa77-3c8c-bb52-7656dfe74840 | -15.51585 | -46.83405 | 2025-10-07 00:11:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1a16dd5f-a67f-3000-bf70-f407d8a272dd | -11.7451 | -43.30178 | 2025-10-07 00:11:00 | TERRA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 7bc1b4bd-d718-313e-9497-a729b3e61984 | -12.32456 | -50.99984 | 2025-10-07 00:11:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 11bf6c3d-59b3-336a-a719-ccc24722cebe | -11.84594 | -45.0664 | 2025-10-07 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| abbb1f69-5f6c-337f-880e-ec5cbc2703a5 | -14.9008 | -51.45547 | 2025-10-07 00:11:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 2663c227-46e7-3f72-ae6f-883e5d309a4a | -14.93152 | -51.4763 | 2025-10-07 00:11:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 149aa9a3-42b4-35fe-85ec-2aa4a45d66e2 | -13.37305 | -44.29891 | 2025-10-07 00:11:00 | TERRA_M-M | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 70ca089e-c53f-3666-8985-3dff7c2de23e | -11.79688 | -45.10833 | 2025-10-07 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 151690f8-d4ed-37b9-8b66-1a03144fc137 | -13.80672 | -41.83155 | 2025-10-07 00:11:00 | TERRA_M-M | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 8a3be29f-9e67-3ca5-abde-4679b50f0bad | -13.66897 | -44.30957 | 2025-10-07 00:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 45.0 |
| bc219e50-fba2-3a6f-be7e-9217dc9f8550 | -11.04509 | -44.78617 | 2025-10-07 00:11:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b6899691-e7dd-3a82-8fdd-3af345229f15 | -15.59426 | -42.35632 | 2025-10-07 00:11:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 37af367a-727a-310f-901d-0f1581989ca2 | -16.13732 | -46.17969 | 2025-10-07 00:11:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 36d8d253-28c6-3760-851e-c47c40de2126 | -11.43978 | -43.48335 | 2025-10-07 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9450d5b4-03e1-38da-a0d1-c4c1a588e291 | -10.09391 | -40.77878 | 2025-10-07 00:11:00 | TERRA_M-M | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 14.6 |
| d8dcca3b-f16b-3a7c-8bcc-987db582094c | -11.79558 | -45.09858 | 2025-10-07 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 268f4316-7922-3afe-a189-4e0f890423f1 | -13.64753 | -47.28768 | 2025-10-07 00:11:00 | TERRA_M-M | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 35cbd37e-cb67-3339-af6c-deb1af2d7c66 | -12.48972 | -45.55466 | 2025-10-07 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7de775fe-b361-3d45-8318-9deab4db6f88 | -12.42591 | -45.62222 | 2025-10-07 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| b033d3e0-1c2b-3d81-8259-6b7aa3f7f724 | -10.26131 | -44.37506 | 2025-10-07 00:11:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 25.0 |
| f46729cf-388e-3c19-83c0-146f825abda5 | -11.60811 | -43.10904 | 2025-10-07 00:11:00 | TERRA_M-M | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 56c43d50-a541-3bf2-8612-922152a18a54 | -10.26007 | -44.36604 | 2025-10-07 00:11:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 38.7 |
| fdb7ae1b-03db-358f-85fd-1ae610f90e42 | -11.71198 | -45.44944 | 2025-10-07 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| bc3f7f76-189f-37da-ab97-3ce9dea1c233 | -11.77193 | -45.13192 | 2025-10-07 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 841a4eca-fb13-300f-a47b-b026e186092c | -13.24917 | -48.05701 | 2025-10-07 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 14.9 |
| a33c4c99-9a12-3c9f-bd4c-04fcbc22f7a8 | -10.2512 | -44.36731 | 2025-10-07 00:11:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| d0f8a91d-8b73-3199-be24-03e4390f82fb | -15.82618 | -41.89546 | 2025-10-07 00:11:00 | TERRA_M-M | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 858b1029-4643-33d8-944e-3e196adab5fb | -14.8793 | -51.42011 | 2025-10-07 00:11:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 3af0a72b-7c44-3f10-9797-426af019aaf4 | -12.85647 | -43.81774 | 2025-10-07 00:11:00 | TERRA_M-M | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4bb16a3e-8732-36b4-8ff4-b07651bc217b | -15.60588 | -52.57549 | 2025-10-07 00:11:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 129.5 |
| b83d452f-62c9-32fc-89b5-c7055b4847bc | -14.89768 | -51.44894 | 2025-10-07 00:11:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 60.1 |
| fed8ddf9-f221-3a46-979b-675407b0edf2 | -13.67839 | -47.33154 | 2025-10-07 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 85fc0b8b-1e04-3d10-990a-1d7591fd607b | -11.78641 | -45.09984 | 2025-10-07 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7004b891-2299-3fdf-a5d8-3f4da9d78e27 | -10.6727 | -44.14804 | 2025-10-07 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0a5331a4-baa8-35f2-bd43-26e19d24d185 | -13.2833 | -48.05198 | 2025-10-07 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 32e578ab-d83f-372b-a062-d437eb9e166b | -11.25231 | -50.26749 | 2025-10-07 00:11:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 3c1662ff-4922-357d-9085-0aa6c1014f29 | -11.50255 | -44.97135 | 2025-10-07 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 896630c3-74a6-35af-9905-f858654c3f75 | -17.54585 | -46.77048 | 2025-10-07 00:11:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4265017d-39e9-30d3-9a1c-877c99436305 | -17.16157 | -43.45221 | 2025-10-07 00:11:00 | TERRA_M-M | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 37bc9408-e5f8-3e6e-907c-afd02b563c60 | -16.30913 | -42.05219 | 2025-10-07 00:11:00 | TERRA_M-M | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 4d682557-6390-3af7-b7d9-8d52348ef275 | -15.76281 | -43.58929 | 2025-10-07 00:11:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 75d8ee1b-a0ab-3209-8b2f-98fd17e20959 | -16.54882 | -42.72947 | 2025-10-07 00:11:00 | TERRA_M-M | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 98c69901-51e3-308d-b915-ea494dfd9a39 | -13.37432 | -44.30832 | 2025-10-07 00:11:00 | TERRA_M-M | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 18108f9e-ffad-347e-b324-5584f5264902 | -14.2827 | -45.84807 | 2025-10-07 00:11:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 393e8ba4-0332-3b99-8211-4db6b920331a | -10.38902 | -45.38186 | 2025-10-07 00:11:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 22f0ba49-b1e1-3469-afbc-f93acafa32cd | -10.27099 | -44.36795 | 2025-10-07 00:11:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 610d3615-09d6-31ae-8ad1-01ebbfa1ff96 | -17.98045 | -44.99872 | 2025-10-07 00:11:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 18.8 |
| c6e2b228-2121-39a1-bb28-a0c33af66b99 | -11.65156 | -46.41356 | 2025-10-07 00:11:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 899a6682-85bb-3703-b82f-2238ffc440b4 | -14.87013 | -51.45876 | 2025-10-07 00:11:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 174.0 |
| 93e78eb0-3fcb-307e-af60-fc153e3b18b4 | -14.65685 | -48.37386 | 2025-10-07 00:11:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 16.8 |
| d6e99c1e-f9d9-3357-bbce-dbe6f46c60c6 | -11.46868 | -43.49738 | 2025-10-07 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 742da4a7-6cef-336b-8193-414d0e43a5c9 | -15.50502 | -46.83474 | 2025-10-07 00:11:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 18.5 |
| fc8d2ab1-87e8-31ba-a38d-25e58870e195 | -11.25486 | -50.28901 | 2025-10-07 00:11:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 74873922-40db-3e79-8499-1b6dacfb6433 | -13.36263 | -47.56897 | 2025-10-07 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a6bba9eb-f9d9-36f7-8ddd-165d86c334b2 | -13.28294 | -47.57458 | 2025-10-07 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 411aea3d-433b-3863-ba33-397d2a589fd7 | -11.80751 | -45.04782 | 2025-10-07 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 9c05fae1-f394-3fa9-b0a8-e1e169bde2f1 | -11.7044 | -44.41715 | 2025-10-07 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c96aaf51-1428-34d8-a197-37da51cfaf5e | -14.864 | -51.42179 | 2025-10-07 00:11:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 28.2 |
| e75d6ab0-ab7b-3c0b-92fe-66d4dd82083a | -16.11182 | -48.9245 | 2025-10-07 00:11:00 | TERRA_M-M | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 24.8 |
| af91e24f-3f27-3cc6-be45-3c8371896294 | -12.34016 | -44.2178 | 2025-10-07 00:11:00 | TERRA_M-M | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2846678c-580a-3d3c-8c30-1e9e986fcd06 | -15.35549 | -47.30312 | 2025-10-07 00:11:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 19d6ecd8-30fe-3fc4-8ed7-98fc2039d188 | -12.16472 | -50.89701 | 2025-10-07 00:11:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 24f72a23-9a16-35c1-9924-79ea14d956b9 | -12.61468 | -44.75175 | 2025-10-07 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| ddfada15-efc2-3d10-9f29-53fb8c29dc46 | -10.27344 | -44.38605 | 2025-10-07 00:11:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4d3cf89b-5f2a-3f15-ab6d-78a5cbfd1e5f | -11.38431 | -43.48821 | 2025-10-07 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d2e52e15-6445-3954-9a60-bbe9e50e3497 | -15.29281 | -46.33851 | 2025-10-07 00:11:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e47be333-94ed-326b-9c88-700501617e52 | -11.38555 | -43.49715 | 2025-10-07 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 1bf4964f-9690-3cae-b89b-581dff015615 | -13.53715 | -42.99874 | 2025-10-07 00:11:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 116.5 |
| 7ddffbb0-240c-3924-b1d6-937d8323c7b8 | -11.70565 | -44.4264 | 2025-10-07 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 9f9e5f15-2df6-3add-bca7-d31744c155da | -10.93724 | -51.17646 | 2025-10-07 00:11:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 32.5 |
| c60de119-8519-34b4-b631-4107a0c1efff | -17.52855 | -42.48611 | 2025-10-07 00:11:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 331f0104-045c-3c1a-a066-a3879aa05438 | -17.54295 | -46.76155 | 2025-10-07 00:11:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 722b66d4-f26b-3598-a1ac-6d66dec5a942 | -14.76389 | -46.02561 | 2025-10-07 00:11:00 | TERRA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 9d92a7b5-26f8-34c3-a6c6-1a49ef6a2824 | -14.86702 | -51.45231 | 2025-10-07 00:11:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 0f19791d-1925-335c-b0cb-28725e2a16d1 | -14.91301 | -51.44727 | 2025-10-07 00:11:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 81c899ae-42c7-3fe9-928f-01aae990fd9b | -16.11409 | -48.94505 | 2025-10-07 00:11:00 | TERRA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 6ea69e4a-497c-3adc-8188-a91fe99eb4c7 | -12.40214 | -51.14331 | 2025-10-07 00:11:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| a7bbabe5-dbbd-33ec-bd08-755ab59d5c40 | -13.28747 | -44.13877 | 2025-10-07 00:11:00 | TERRA_M-M | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| beee5eb6-ac2e-31fb-b538-af7e88496ec6 | -15.65402 | -43.66869 | 2025-10-07 00:11:00 | TERRA_M-M | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 84ef1ac6-23e8-3035-b55f-5023e5b54e58 | -13.784 | -50.78834 | 2025-10-07 00:11:00 | TERRA_M-M | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 40.8 |
| b7cb2dad-d7a2-3584-9842-05d30f0c9170 | -14.70942 | -45.99657 | 2025-10-07 00:11:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 1c58c1d4-4e9e-3320-99be-27a65d5aa576 | -13.27639 | -47.16421 | 2025-10-07 00:11:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| bb5b1dbd-f9c4-35dc-80fa-78a8f853aad7 | -11.94085 | -43.04479 | 2025-10-07 00:11:00 | TERRA_M-M | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 35.7 |
| b6112b23-886a-31e3-9584-1174a93dae23 | -14.88235 | -51.45062 | 2025-10-07 00:11:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 154.3 |


[Clique aqui para ver as próximas entradas](README5.md)
