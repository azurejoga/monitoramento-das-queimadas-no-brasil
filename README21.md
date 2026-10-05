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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da7cadef-3a2a-34ec-abfc-c5b6faef4063 | -2.94366 | -54.12975 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 989e1140-377d-3ad2-b219-8a2a45c0043d | -2.68661 | -49.03511 | 2026-10-05 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ea6ae932-b79c-3b47-a652-7fcfe54009ad | -3.15148 | -50.44249 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f82504f3-febe-32ae-9e11-e8a3dd387ecc | -3.10688 | -53.72416 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a61f6822-9d69-39de-a68f-84c7dcc16977 | -2.95202 | -54.14418 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 689dbb62-7b94-3eec-8ab6-1e9d0f6f6608 | -3.71434 | -40.34641 | 2026-10-05 04:38:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8b3ca008-bb73-31ef-8b16-f55be9e00092 | -3.84364 | -55.84281 | 2026-10-05 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de88c4e7-aecd-3d0c-bb68-54e3c1314538 | -3.50469 | -54.61394 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b916fec-68b1-3eb2-a7e0-20ff14cd5bde | -3.11912 | -53.76278 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| a172f6ef-37c3-346e-a09f-e7e168500b5b | -3.08573 | -54.17825 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 9a857a20-1adf-3707-a3ac-b60a68180e3e | -3.12104 | -53.721 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2869f558-0f77-3d58-a64d-35978225990a | -6.42898 | -43.72018 | 2026-10-05 04:38:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1bd5bcce-d756-3d33-9556-35415d366014 | -3.27733 | -50.02161 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0707db0a-dcf8-3384-a624-c7fd47db4b6a | -6.89836 | -43.66681 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bea327d2-af00-32d7-afe8-000676613022 | -6.9319 | -43.67884 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 67b6e07c-d80c-3efb-b843-94991ddef9ea | -2.9015 | -54.12561 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e17751a-b46f-313c-b552-795069fea47a | -4.40402 | -49.63871 | 2026-10-05 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 12116c1d-d1e9-37f8-8cb3-a455c8d637f6 | -6.60066 | -41.56091 | 2026-10-05 04:38:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 11a2e778-c167-31d0-81f0-49c40eedb6f2 | -1.45547 | -53.59604 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca519ac1-0136-35e5-b718-870afed9d347 | -2.22532 | -53.70613 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36ae5b92-5916-3ae2-8d11-def63f841d94 | -6.90891 | -43.66304 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 018497fe-dbe6-3c92-bae6-82a50742c133 | -6.61255 | -41.56268 | 2026-10-05 04:38:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f547478c-7c89-3052-ab5c-2d23b1264b49 | -3.05056 | -54.22735 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ff640689-7232-35ae-bbfd-ab73b2e22784 | -2.89681 | -54.1216 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9f71051-42cc-3375-a2d3-c0fdb3b97fb6 | -2.94005 | -54.12163 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50afc2b7-3692-3f78-8c74-d59c74e3ea08 | -3.33032 | -53.39394 | 2026-10-05 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5937b84b-c8ea-312d-92eb-7b751245970b | -3.2744 | -50.40109 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 43cbbc78-b5a0-3985-8769-5c4a186d5da2 | -2.79688 | -54.11128 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c65e5075-c712-3c76-8169-faf57ec621ef | -6.00572 | -53.51041 | 2026-10-05 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 74d950b9-e09f-325c-bce8-c7b8baa8edca | -7.89418 | -44.19207 | 2026-10-05 04:38:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aad4f126-62ef-3dd8-aa9d-dde4d41e5ff1 | -1.61664 | -55.14037 | 2026-10-05 04:38:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a30732fe-ed8c-3693-9940-6f4ecf3db755 | -2.99058 | -54.10762 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 886dea43-d507-3c94-992b-9bed7af85929 | -2.94697 | -54.20694 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae522b42-9189-3257-812b-64d65b38ca42 | -3.07424 | -54.18276 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 1e93ee77-2c34-3d63-8c61-a6ee59bac2ad | -3.20498 | -50.74526 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d01ece42-2379-30a8-88ca-8c2a136e2d75 | -3.0669 | -54.19444 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4700c618-8b06-37c2-973a-190fdcaf9c60 | -7.4835 | -42.80218 | 2026-10-05 04:38:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0208a645-9306-340b-af70-a65ad768deb9 | -3.29759 | -49.12703 | 2026-10-05 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 676f3111-38cb-396c-b52c-fc9ab47d9fa8 | -3.2742 | -50.01606 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 388ac67d-7c65-302b-92e3-6ad6aa60d043 | -3.12965 | -53.73146 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36583d3e-c86e-3a54-8e8b-38def845076e | -2.9387 | -48.48486 | 2026-10-05 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c098591-29d4-3742-9301-b0c87d2593e9 | -3.11505 | -53.75608 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f8848737-dfc3-393e-941f-beba08d8815d | -3.58956 | -54.30945 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5c8d6fbe-839e-3324-a753-f2d0f432d544 | -2.85228 | -51.2926 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 156a72c6-6d76-301d-9ba5-067d478a75f9 | -2.78748 | -54.10335 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2e86bbdc-73d6-33b6-9420-4b3b489ec9ac | -3.90721 | -49.6982 | 2026-10-05 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f6803de5-8398-36a9-a5ce-88b333a1eb55 | -1.74812 | -55.24094 | 2026-10-05 04:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7206308a-d3b1-34cc-ac83-55f901122f19 | -6.91653 | -43.68464 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26fabd0c-3640-3073-ae65-dee409761873 | -3.09479 | -51.09981 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6eb5f6e2-b3f2-3193-b52f-951448e4b595 | -2.91244 | -54.12424 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 364cbb86-ced7-3ef8-85ed-779fd127f042 | -3.10784 | -53.7183 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 8d189518-a38f-3082-9c51-54f7cf9fc6c8 | -2.81304 | -54.1108 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 321a2007-694a-3cf1-82f9-d41a08725347 | -2.95304 | -54.13793 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e1f46eaa-9265-31b5-8c44-75d493b15bcd | -2.99115 | -54.04083 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ea13b73-acbb-3a56-b4ba-65d1d2e36a50 | -6.17966 | -52.9371 | 2026-10-05 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33517b1c-6261-3099-81fa-b76e8859ca0c | -1.09784 | -54.11955 | 2026-10-05 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a38a5d5e-9365-3976-ad5e-f0f29e305375 | -3.09678 | -53.72243 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6ea0d723-e39d-3614-8431-d461380ab0f8 | -4.10824 | -49.07619 | 2026-10-05 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 494c755c-8668-3c0c-980c-154948ce5acb | -2.80523 | -54.12562 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff379ba8-b617-3de0-b9ad-44e8de4df29e | -3.11299 | -53.73769 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f18aff3-3678-3284-bf37-eced912b4c76 | -2.67541 | -49.03331 | 2026-10-05 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| cb11a825-f766-34b4-b003-9262f54f3521 | -2.99876 | -54.21913 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4a0a5c1-d4a3-3931-a9ab-a1222e763893 | -1.10003 | -54.10588 | 2026-10-05 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 389f876e-3d72-31e2-9f22-90094ef19985 | -3.88458 | -55.81199 | 2026-10-05 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a184364f-90f4-38b4-959a-fe39729cd93a | -3.1088 | -53.71245 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 33fc144a-ae37-3331-ad22-adb147221e7b | -1.61729 | -55.13649 | 2026-10-05 04:38:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8a0426a-b8fe-3cd6-abe0-cedd30a49088 | -3.04647 | -54.22351 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a7429d18-772c-3fc8-8582-5508ae18f3e5 | -5.94839 | -41.3185 | 2026-10-05 04:38:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| df3e780e-0a17-301a-847a-46829e6ff6bb | -3.5149 | -54.63272 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 629cd991-8858-35e0-b66d-49b239d04b99 | -1.46008 | -53.60017 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01cb2dd7-ca0b-378f-879d-e78461a785ce | -2.48444 | -56.09717 | 2026-10-05 04:38:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cd137f7a-10ae-383d-8f05-cf6c13f960ff | -3.10811 | -53.74841 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 655a5364-e2ae-3213-96d6-dbf77d1ea3b3 | -2.16614 | -53.66788 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9880b23-bd63-3fa3-8456-8eb586c6c144 | -3.18314 | -54.08112 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69725f56-d516-342f-842c-820891bb408a | -3.92006 | -49.71527 | 2026-10-05 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 72c6e222-c285-3ca4-a846-d0e96030b8b5 | -2.94831 | -54.13599 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 27f5b175-9241-3ff0-aa60-813db5a22eae | -3.70778 | -50.64549 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e8f188fb-ae61-306d-b3ff-268c9c0a9753 | -3.15841 | -50.45078 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94940b06-3d9d-30bc-8fe1-7adc087462e7 | -3.51174 | -54.61861 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e410e793-4aaa-3dc2-81ea-591bc77b74de | -3.29018 | -50.30522 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 30585161-1464-3b55-bfa3-cea9e0167837 | -3.16012 | -50.4404 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63171c59-78c5-3f4c-a547-68a68b398125 | -3.07529 | -54.17654 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 46787061-ec7e-34d5-a068-eb55a93e04da | -3.37244 | -54.0974 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5c8b82f-625c-3aae-b256-d82d8e22665b | -4.46516 | -54.96187 | 2026-10-05 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51d3d9b7-3127-3e50-8afb-03d036469f29 | -3.11524 | -45.18935 | 2026-10-05 04:38:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3b52e8d5-8da3-372d-9656-8c2f8fd8a0fb | -3.12133 | -50.34426 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa275ce1-73d7-3da8-a7c7-8c7d1c724703 | -3.84114 | -50.31574 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 25a68528-a4c1-3111-ac34-80a162d5bf5b | -6.15796 | -43.63214 | 2026-10-05 04:38:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 91a4ffdb-1b3d-35ca-9806-d860a650364d | -3.26303 | -52.25221 | 2026-10-05 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 21874092-3959-3ded-8903-75b89c59848b | -3.31272 | -53.84159 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d02d1961-cf62-36e2-afd0-f6e3121747cc | -6.00398 | -53.52048 | 2026-10-05 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3be049c8-9a15-37b1-ac68-b0f90b15d762 | -3.0912 | -51.09524 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6cc33f4e-93bb-3f3e-8f47-34187a069ef7 | -4.1101 | -49.07897 | 2026-10-05 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 05a00e0c-b0d2-33cc-bb46-c6f57317b1de | -3.11649 | -53.71726 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61542f4c-901d-3dd4-b272-1c0d6bca817c | -3.11269 | -53.7522 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9436b99e-70d2-3123-9046-eda9679f97aa | -2.81356 | -54.10765 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0342e941-c5b4-3523-ab3d-8b400c1936a6 | -1.12774 | -49.23129 | 2026-10-05 04:38:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a47f9eb8-23c4-303b-b633-da5dd1a53625 | -3.2188 | -53.87161 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d2731f9-1b61-3dab-b5d6-b2f07939ebb9 | -3.29268 | -49.51357 | 2026-10-05 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99d07541-11cb-3a16-9c8b-8c46eaf87016 | -1.61442 | -55.11028 | 2026-10-05 04:38:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README22.md)
