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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c6c50da-f9d4-3407-8caf-8f297709d6c6 | -3.77051 | -61.77511 | 2026-09-05 05:59:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e1cf76e7-74d6-32a6-bd0f-0fe7d000b141 | -3.76717 | -61.76871 | 2026-09-05 05:59:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b4603704-2be7-322b-a7ff-d2648749a9a7 | -6.65529 | -59.94485 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| de5bf941-74d0-3080-8463-856f560da4ab | -5.83634 | -60.2523 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6d51dcd8-eb3b-3287-ac3f-1df3c7a03bf8 | -4.66418 | -55.64052 | 2026-09-05 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f6736e87-7c6f-3ec9-9e5b-b77805035244 | -6.6566 | -59.93538 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f2d8186-1a5b-3ed3-a4ee-5784509e1064 | -6.6657 | -59.94649 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1a6ee19e-fc87-30ed-822e-9e7cc9d173ca | -6.20149 | -57.77262 | 2026-09-05 05:59:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5791b20-40a2-3c22-8e01-cca955257466 | -3.8032 | -55.88289 | 2026-09-05 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf6a01ed-8d51-3d38-b410-11499a6e4d28 | -3.82439 | -60.76649 | 2026-09-05 05:59:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e1770de1-b0cc-36c1-9257-49561ddc117b | -6.65395 | -59.95446 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 03fe125d-c871-3bf3-b1bc-851241858e01 | -6.68218 | -59.98051 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4821a1e-ad12-3024-8098-d7adf4fbdb27 | -2.59282 | -59.40288 | 2026-09-05 05:59:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad1296a9-97f9-33f0-9cca-d04bd5696e63 | -6.6544 | -59.95125 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 18.7 |
| aa662654-273f-3a99-b4d3-3d69ed43c9a3 | -5.34071 | -56.02196 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| bcb9de68-b2a2-3691-b118-f74397b9f234 | -3.82711 | -60.76951 | 2026-09-05 05:59:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8153d982-3484-3f59-a1ca-502f23769091 | -3.72131 | -59.36677 | 2026-09-05 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a1ff5eb-1b43-31e4-8238-58c0934f80da | -5.31937 | -56.03037 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d1409b2-26c2-33f2-b0bf-467147b28837 | -3.76342 | -61.76382 | 2026-09-05 05:59:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 20402fb6-6009-39de-933d-807ed99605dc | -6.64964 | -59.94719 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 18.7 |
| be03c5ad-9e07-3e7e-a07f-fafab402d7e9 | -5.25246 | -59.97766 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aae3a4b6-6bf0-3b0b-8df1-a1daaa2160c9 | -3.07953 | -61.17707 | 2026-09-05 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b7109106-16e2-3fb6-9368-576c1aa8d99b | -5.30696 | -56.02302 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f167595f-398d-3325-b105-8e18267f2328 | -5.43195 | -60.18727 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 732b1eb6-11eb-3e49-b7f4-f6fa3251d49f | -4.6816 | -55.63865 | 2026-09-05 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9c4e9394-438b-328e-befc-68fe865d1357 | -4.67176 | -55.63504 | 2026-09-05 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b66c60fa-7746-376a-83fe-e33713c7214a | -6.65351 | -59.95763 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.8 |
| d021b9ac-fe96-3433-9fb2-b61c24a89fb3 | -5.35134 | -56.03164 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b7e62cbe-d724-3f74-8d16-6cccf826b6eb | -5.32594 | -56.03136 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 672a224f-2032-3a2b-9071-7332b7bf1c67 | -6.65307 | -59.96082 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b9b7b59-782c-3aec-80d4-132925b3d344 | -3.77222 | -61.76512 | 2026-09-05 05:59:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0969397b-2739-3ebc-90f1-500d3541745c | -4.66497 | -55.63478 | 2026-09-05 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| cf8e82d3-0d46-34d6-807e-a3b72e11ccdb | -6.66005 | -59.94886 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e36ede86-db5d-3a51-91e6-f2d101450626 | -3.92879 | -59.34151 | 2026-09-05 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c647a7c-4205-3726-9423-e9b82ee84086 | -6.68314 | -59.93598 | 2026-09-05 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8cb9d89c-e47e-3f10-86ff-0cbe1fe7cb38 | -6.66092 | -59.94258 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7f3fbd8a-e061-3854-8c47-38803903fc7e | -5.56155 | -60.17417 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a3ca071-bc90-3d81-9e0b-1aa4bf0ac1be | -5.46224 | -60.04722 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e818fae1-83e5-3e7d-9a67-b6811b225888 | -5.3465 | -56.02857 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5d550f30-2083-3d11-a621-b4c856045425 | -3.83182 | -60.77026 | 2026-09-05 05:59:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 194e9b30-52dc-3fd0-9c8e-5268f598e292 | -3.93312 | -59.34479 | 2026-09-05 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d2b8ba77-3aa3-3a89-b294-af9ffd747ae1 | -6.66136 | -59.93944 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72803198-80e9-3af7-a262-f5ed8a68441a | -6.12761 | -59.92775 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e54d5aa2-c03c-3671-99ba-210c5b34aec4 | -6.594 | -59.92286 | 2026-09-05 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdc976b0-216f-3f05-88c6-621626dc8378 | -5.76785 | -59.19138 | 2026-09-05 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7767bbcb-7d01-3035-a526-b6c7ab5fa0fe | -5.55692 | -60.17049 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8ee52c89-5411-32fd-bd07-507ff8a2f9a1 | -3.7753 | -61.7743 | 2026-09-05 05:59:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9e46c875-a1b5-35ca-9b00-e4e22b60f2bc | -5.43058 | -60.12426 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f37509b-e07e-3b3d-a909-c54fbc7cfccc | -3.79739 | -55.88064 | 2026-09-05 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c796cbee-64f4-3c83-9f2d-87d7cdc9e4aa | -6.6926 | -59.9819 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b59bd376-f9ae-3048-8287-4fdf4b1f1157 | -2.85296 | -67.28617 | 2026-09-05 05:59:00 | NOAA-20 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f35c4f1-774b-306b-a5c5-d1422b1237b0 | -6.65008 | -59.94402 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ac01438f-8001-35c4-ba06-2b2700f3fbd4 | -5.29533 | -56.00999 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7e86ca77-4fe0-321d-8adc-b256e9406401 | -6.6698 | -59.9443 | 2026-09-05 06:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 157.8 |
| 5997636a-9240-3778-8b33-f1c7c815b3df | -6.6697 | -59.9635 | 2026-09-05 06:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 322ce9aa-7041-3265-8ecc-6f14a6475e88 | -6.6514 | -59.945 | 2026-09-05 06:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 146.2 |
| 2290e5b0-eef3-3a66-8374-237e81f6943f | -6.6513 | -59.9642 | 2026-09-05 06:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 4b14cc1e-910f-3df5-b77f-a13e52965ad1 | -5.346 | -56.0454 | 2026-09-05 06:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 4b890e1f-310e-35f7-913b-0c2edc63ae81 | -3.7645 | -61.7737 | 2026-09-05 06:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 1a3305f1-ac76-3024-b003-687e02a09ca4 | -5.3462 | -56.0256 | 2026-09-05 06:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 54b85398-733c-31ba-947a-d7db020bca0c | -6.97441 | -71.65984 | 2026-09-05 06:01:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e46d54ea-6dbd-300a-8602-2fe31feae07f | -9.84448 | -68.97585 | 2026-09-05 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4d4f3c7c-9bfb-3809-ae34-ca54b4d331f2 | -10.12194 | -68.28617 | 2026-09-05 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 462ec158-7060-342a-a96c-eb4713d6af2b | -7.5618 | -61.41657 | 2026-09-05 06:01:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5dd3767-a5f5-3c95-b9cd-65da1a03999a | -8.77214 | -69.57262 | 2026-09-05 06:01:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cddf15f-731b-31b1-9f20-8bdadf4045b1 | -10.23072 | -68.65399 | 2026-09-05 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e867d90d-c2e3-335a-a76d-9643be9098b5 | -9.13095 | -67.80775 | 2026-09-05 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5e3b067c-2962-329f-b46d-fe8236e2d87e | -10.20021 | -69.08994 | 2026-09-05 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf929bb5-0c4c-3931-a93b-929352fe73a9 | -8.96533 | -69.27533 | 2026-09-05 06:01:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6bdbe63c-977c-3567-9beb-86f1ae99e25d | -9.80332 | -69.08768 | 2026-09-05 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14ec4a53-ac01-3cba-a1cc-9312e0944f75 | -9.00659 | -71.92915 | 2026-09-05 06:01:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f08b99d5-4d0b-3cfe-9fe0-948f8b012bac | -8.96864 | -69.27586 | 2026-09-05 06:01:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5102bb38-acc9-3f4c-a94c-a03613bb7e5c | -9.04423 | -70.73192 | 2026-09-05 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35a62e9e-1f19-36db-8fd3-ffaa75b32e88 | -8.84557 | -70.87241 | 2026-09-05 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e36dca5a-cb7a-3cfb-b543-e1e636e369c9 | -8.82637 | -70.79787 | 2026-09-05 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 814e5654-f4e1-32db-a16f-a31920855e5a | -9.41727 | -68.99391 | 2026-09-05 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8554135-97cd-3dae-a823-d2c4b557ddb6 | -10.16667 | -69.34635 | 2026-09-05 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c930aa58-074a-3267-837b-e4e8e3b6dd93 | -8.49912 | -70.49548 | 2026-09-05 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d4e96e65-a564-3aaf-8b73-aa066a1a259b | -9.1049 | -70.83491 | 2026-09-05 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 98871d26-da16-359e-b579-6d872d9cd949 | -9.46394 | -67.41936 | 2026-09-05 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7646008d-9f6f-3f88-8b14-33dbcac26457 | -9.13376 | -67.81192 | 2026-09-05 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 00f473f7-8df3-32d7-9310-b8c2197b59c6 | -8.86523 | -68.48631 | 2026-09-05 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3927c9de-9f59-3422-b96a-358fce9d609a | -9.13489 | -67.80465 | 2026-09-05 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| caa6ebd9-b920-3764-9f7b-1510f7766aad | -8.81135 | -70.53873 | 2026-09-05 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5786a179-d5e5-325b-8e0d-f49221bfc334 | -9.02637 | -70.71408 | 2026-09-05 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 268c8060-a6f0-3400-bc10-7676681919d7 | -8.74449 | -69.59641 | 2026-09-05 06:01:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc08cc69-7e3c-3ddf-9e7a-31a6277e08d1 | -8.88769 | -70.54764 | 2026-09-05 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9ece079-521d-33f4-8bc0-765e5d616c65 | -9.52805 | -68.63416 | 2026-09-05 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c6c83e9e-bce1-3f0c-96f1-1bcb698d5ed4 | -8.86856 | -68.48684 | 2026-09-05 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3f54ce2-5585-3468-8eac-fe76ae0458e8 | -9.33444 | -68.89478 | 2026-09-05 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b2f7925-22e2-39a5-a499-ef1d8298a4e7 | -11.90667 | -64.99613 | 2026-09-05 06:01:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 10ff4785-ffd7-3825-ae58-50ed39f96fef | -8.96477 | -69.27881 | 2026-09-05 06:01:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 747a312c-4a64-3075-b269-44b91da7347e | -8.77269 | -69.56912 | 2026-09-05 06:01:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ac0562f-a48b-38b9-87f2-1c1c4f901bbf | -9.75116 | -66.61925 | 2026-09-05 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29c063e6-1bf7-3341-9a60-9ff088aff012 | -10.91227 | -68.32297 | 2026-09-05 06:01:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 09a881a3-335b-30db-b2c2-a381b1cf9aa1 | -9.53193 | -68.63116 | 2026-09-05 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc6ba42a-ea83-36ac-a64c-266c08d282fb | -12.00921 | -64.88776 | 2026-09-05 06:01:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bbfacf7e-a99f-3721-a010-934cb913932b | -8.86566 | -70.66257 | 2026-09-05 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2d10dbe8-dfa2-3fd7-864a-691df3e4e1a3 | -8.87133 | -68.49089 | 2026-09-05 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68977c04-b257-3adc-95c4-45d7f7ccab75 | -9.18836 | -68.26209 | 2026-09-05 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README35.md)
