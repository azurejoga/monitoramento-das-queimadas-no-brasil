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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ce71c6b-b0e0-3e35-b198-8c59aca7e7be | -2.44821 | -50.25023 | 2026-10-05 17:15:00 | NPP-375 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 661bc78d-c81c-3c56-bf0c-649bead4d5e9 | -2.48756 | -49.41368 | 2026-10-05 17:15:00 | NPP-375 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 3b6657ce-ac25-380a-ac0c-0a2760decdb5 | -7.22539 | -55.1861 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 384d65e6-c8d4-3578-be19-be54f6f8d9d7 | -9.11037 | -65.35259 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 59dc19de-abf6-3b82-b660-7b1d8115e38c | -3.67825 | -55.94114 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 7e7df374-e56f-31f6-a7dd-c6b055baeb11 | -5.72855 | -53.61536 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9c6ce602-dfcd-3f7f-af1f-e3eec9b58f5f | -3.04556 | -54.22113 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 21032c09-7f07-3799-95c7-08b4df69dd4d | -4.27709 | -55.13308 | 2026-10-05 17:15:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| fe86ed14-127a-3590-8249-eaee36b9b531 | -3.09611 | -53.71684 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 113.3 |
| bd5938f3-11d8-3d04-92b2-cddf5afb9024 | -2.99108 | -54.10933 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 25275b7f-71b0-3c67-88e7-8030052c2f7a | -3.52514 | -54.32859 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 05a221ae-a8b8-3242-953c-e442ef90c54d | -3.00316 | -53.87757 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c5b6b42b-e113-3239-bac8-35f14e5db148 | -4.79966 | -42.14267 | 2026-10-05 17:15:00 | NPP-375 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| e1cf0c51-6196-39d7-9226-b4eb2f0b6309 | -3.56387 | -44.56897 | 2026-10-05 17:15:00 | NPP-375 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 3325de58-5d2a-336f-b5d1-49439593e98d | -9.61863 | -65.36835 | 2026-10-05 17:15:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 8679dffb-d725-3888-b5d9-f8f6deab2fd6 | -4.41184 | -55.11571 | 2026-10-05 17:15:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| ea66be4e-ea16-34b9-ae2d-2b614961f786 | -9.40852 | -65.89558 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 15bb1c8a-66b0-354f-b8d4-ff37cea9ee94 | -4.1209 | -54.42208 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 0b4bb5fe-c6aa-38fe-a638-f3bc2ece9029 | -8.6585 | -54.55624 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| f4d3ea7b-3bf4-3c51-94bb-76b5a5d8db7f | -3.88507 | -58.95539 | 2026-10-05 17:15:00 | NPP-375 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 1b94bf93-f7bb-3fcf-b235-b9c05ac92f0a | -6.91339 | -59.26014 | 2026-10-05 17:15:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0b0f857b-6647-3118-a12c-84bbc5ebb598 | -2.99046 | -54.03881 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9e8fca64-1134-3e66-aa4c-4d7f0c643c90 | -4.36785 | -55.42496 | 2026-10-05 17:15:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| ed152a78-a07c-3344-b1d1-2b9d1582f3ce | -4.00115 | -55.67667 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 9d378df4-485f-395f-ac9b-41065ec1146c | -8.22982 | -54.69626 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| cb8aa682-cef9-30c5-a6de-1a9b04d45280 | -8.27647 | -45.92086 | 2026-10-05 17:15:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| a7475252-e303-35d5-b3e7-3900b26c0237 | -6.85236 | -41.79836 | 2026-10-05 17:15:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 28.1 |
| 38c4e202-4e05-39cb-a138-0bb26f24f44e | -5.81438 | -53.84317 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| e4035422-9817-359b-aa98-542a6517f69f | -6.74486 | -55.07196 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 632c2f44-aad6-306c-bd39-de8bc74be928 | -3.22537 | -53.87119 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 14805132-22f4-3a41-b416-881b8364c469 | -6.8056 | -39.29686 | 2026-10-05 17:15:00 | NPP-375 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 22.5 |
| bc8098f7-c32a-33d0-8f9b-c39f9e6fbf41 | -3.92273 | -43.12379 | 2026-10-05 17:15:00 | NPP-375 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| ba108517-3387-3989-9f38-4c45d558ec63 | -9.34736 | -65.8474 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 40036120-3576-3e17-b47f-150ec9d70a43 | -5.69692 | -45.53875 | 2026-10-05 17:15:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 246366b6-20d6-3988-929a-6c09da3b826d | -4.21799 | -53.62127 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| bd37351a-32a8-3d1b-b0b5-349daa102788 | -3.37846 | -54.10098 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a2e730a2-2a0c-39a8-9eea-f3e8d084240f | -8.65782 | -54.57495 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8b2190e5-97db-38e8-bc3a-16d11067e54a | -4.21166 | -53.46928 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 48b618cf-0d84-3d10-af7e-86fb1225af79 | -3.09333 | -53.71404 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 9da6e3c5-d5e9-3646-a8ed-ddd049dcb629 | -8.86161 | -66.79061 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 5f03a6c7-6a7d-3a0c-8c91-9896ed7c5192 | -3.97374 | -59.3379 | 2026-10-05 17:15:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| affe3181-1dab-368e-80da-b723fd60cfc9 | -4.33251 | -43.8215 | 2026-10-05 17:15:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a16b0dfd-e724-38e2-8821-f15116ea8016 | -4.44405 | -54.96676 | 2026-10-05 17:15:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 9adb4db5-771d-32f5-985e-66de80ea27e7 | -6.26314 | -52.84876 | 2026-10-05 17:15:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f3da62e2-eb3b-3b6e-b155-c663b549009f | -4.72114 | -45.20839 | 2026-10-05 17:15:00 | NPP-375 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 815ddb4f-66e3-331d-ba7e-8a36a90c04eb | -3.2964 | -53.84914 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9fb68b1b-4a67-3f04-a9ec-b591d7104001 | -7.20987 | -55.19579 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c7c3ee5a-8db7-3a2a-b3e3-968d0e3324eb | -8.16927 | -44.41899 | 2026-10-05 17:15:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eaa79216-1044-36b2-973d-c03719384490 | -7.90091 | -44.18757 | 2026-10-05 17:15:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 34dceb43-60cf-3753-b261-9bedebb44c55 | -8.78015 | -47.55228 | 2026-10-05 17:15:00 | NPP-375 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| be072788-c478-3409-bfd5-3256a9abc42b | -3.51127 | -54.61399 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ec0209a8-5c59-333a-8de3-ad0f5000677b | -5.39641 | -54.45243 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 3246c8bf-b36a-3f4a-8ffe-cad3aaab8dc4 | -4.44686 | -54.96276 | 2026-10-05 17:15:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| c25439a2-7bc6-3518-8d0a-efe58a898b46 | -3.50184 | -54.61897 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| b2de83e1-0077-39f0-aedc-90265be9e2fc | -3.12942 | -53.71178 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| f3c65625-3cbc-3a76-845b-8fe5b77f3ba2 | -3.07815 | -54.16961 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 898100b3-ddc8-3dce-a198-fe4acc12277e | -3.01308 | -53.23441 | 2026-10-05 17:15:00 | NPP-375 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 77eccc24-1ad8-39fe-9415-8776acfaf495 | -6.68027 | -45.23183 | 2026-10-05 17:15:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 310bde80-bc92-3d63-9613-d55c27b12676 | -3.28841 | -42.25656 | 2026-10-05 17:15:00 | NPP-375 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 155e954d-43fb-3b74-9f71-a15b557f6309 | -3.98245 | -59.34034 | 2026-10-05 17:15:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 88b813dd-6826-36e6-a616-975dd4838b86 | -4.06057 | -54.04969 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| e305cf13-1151-3027-9977-e6b7a3e7f4de | -3.23312 | -53.88001 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| abcf979a-2dd8-3879-908b-4beb11ddf908 | -4.02969 | -54.88492 | 2026-10-05 17:15:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 81d11a86-18ab-3d80-821e-ed321131d4b2 | -3.07762 | -54.16616 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a7832ca0-5f00-33ab-ab1a-512c9e7a552c | -3.37899 | -54.10443 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 664ef653-5b6b-3395-9e1b-a30ddc5ba839 | -3.12502 | -53.70533 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 97505034-a40d-3cbf-84d9-826b3e295743 | -3.88032 | -45.77433 | 2026-10-05 17:15:00 | NPP-375 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ee2735cd-fbc9-3c81-aedc-4769ad32acb7 | -8.30902 | -54.66947 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cca57a73-6956-3dbb-8b32-00edcce8771c | -3.0837 | -49.53592 | 2026-10-05 17:15:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 04ba623b-5811-36c8-b629-e13b897aa6df | -6.31948 | -43.34357 | 2026-10-05 17:15:00 | NPP-375 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 280d3a1e-2686-35e2-bb32-aca4a2cfdd45 | -3.5755 | -55.41926 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fa250811-8a52-3285-8bba-c469950f4d4f | -4.48485 | -43.91226 | 2026-10-05 17:15:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6c270f67-1bae-302c-9b73-df5d013b0052 | -4.06441 | -54.05265 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| ede91e47-b115-35dc-845c-c0a3509a6623 | -3.05061 | -54.20977 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| d286b819-cc10-3315-9165-701a2d179130 | -2.99325 | -54.03485 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 5b287287-0c65-3f68-a18b-218492fd9657 | -3.01984 | -54.1862 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 78c833ca-05b4-3c06-8328-76020c2cca08 | -3.51723 | -54.63078 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 125.8 |
| 244c0fb0-c511-3e78-99fc-a3930f0407a4 | -7.48257 | -44.43177 | 2026-10-05 17:15:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 739e1cef-55bb-34c1-a391-e0e08d07917f | -6.36366 | -43.59409 | 2026-10-05 17:15:00 | NPP-375 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4191eeb2-bf14-3b96-8199-24eca38fef00 | -3.95279 | -42.97201 | 2026-10-05 17:15:00 | NPP-375 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 21fd61b7-8fd7-3ba9-a199-1be6c7969c46 | -8.22928 | -54.69262 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| e6f8680e-940d-305e-b22d-f069bf02de34 | -3.37461 | -54.09803 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c55b366a-b660-34eb-80b6-94df57e5ee03 | -3.05774 | -43.39527 | 2026-10-05 17:15:00 | NPP-375 | BELÁGUA | MARANHÃO | Brasil | 2101731 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ce864da7-bf61-30f4-b122-e0d7cb4fdb21 | -3.82193 | -41.8015 | 2026-10-05 17:15:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 8fe72793-e206-31f1-9fef-9a49733ef39a | -7.09471 | -47.27053 | 2026-10-05 17:15:00 | NPP-375 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| b0f30196-cffb-368f-b820-df63318c7f9d | -2.85032 | -51.29523 | 2026-10-05 17:15:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2c1e78d0-888d-3767-82e8-5ce59799218e | -8.16982 | -44.42199 | 2026-10-05 17:15:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 675160dc-a1f2-3ffe-a35d-374d138b1eed | -5.95958 | -41.36726 | 2026-10-05 17:15:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 174.8 |
| 9786fd08-192b-3896-8103-12089875f382 | -3.07045 | -54.16372 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3e7b9b15-1832-3d96-a2ce-d6d118844b5a | -8.87231 | -66.99807 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 6f1f11ea-aa46-3ae8-958b-88ed375526f0 | -6.64643 | -55.32249 | 2026-10-05 17:15:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 44ebac18-5d03-3362-a20f-c7c0ad806f32 | -4.05792 | -54.03243 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a97c4076-328f-3c9e-b396-b441b9758021 | -3.29972 | -53.84863 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d58cf0a5-9e23-3b19-aeb0-dc404cfd4567 | -8.78622 | -47.56298 | 2026-10-05 17:15:00 | NPP-375 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 5e245a08-d431-321b-9320-f4518431f0a6 | -3.50463 | -54.615 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 444b10e0-83db-3419-af90-edd150803821 | -7.07802 | -40.08952 | 2026-10-05 17:15:00 | NPP-375 | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| b998c796-53d5-3c06-9202-6a439e7dfc25 | -8.84734 | -66.79242 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 23.4 |
| fbd091bf-5705-3666-bf03-192439ba303a | -3.69466 | -55.95745 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| a9dbb323-2042-34a2-9c96-918539e49eb4 | -4.38162 | -43.93562 | 2026-10-05 17:15:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 50a2f3ed-d7b5-362c-9838-9eeacc0073aa | -9.73524 | -65.08477 | 2026-10-05 17:15:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.7 |


[Clique aqui para ver as próximas entradas](README112.md)
