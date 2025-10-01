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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a2aa5bc-f7a4-3874-873c-3f880abd6d85 | -8.58312 | -44.74052 | 2025-10-01 04:49:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e7c9514-f317-3032-8e74-a1e4a317e18a | -6.81271 | -44.47196 | 2025-10-01 04:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51089f23-2ae6-33fd-8289-8248b2f27be4 | -8.75467 | -45.92857 | 2025-10-01 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 91136c93-7b4e-3799-affc-83f1952f9bb6 | -7.79898 | -46.7517 | 2025-10-01 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 79cc66d1-ead4-3b74-a500-500d1c0f1790 | -5.5402 | -51.43738 | 2025-10-01 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56149a29-06fe-34b5-abd2-e1c9196453bb | -6.57817 | -51.68055 | 2025-10-01 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68f25f20-a5f1-394f-b4ad-62710f21c5c1 | -7.41651 | -45.41387 | 2025-10-01 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b858a18f-a1f2-3d85-a34a-fbf2a5e98a96 | -5.98428 | -42.65343 | 2025-10-01 04:49:00 | NPP-375D | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f540584d-51f9-3ab1-8920-b9960d062ade | -7.4681 | -46.46053 | 2025-10-01 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 65f06a23-791a-3882-aac6-7f0e4f31a476 | -5.46923 | -43.07851 | 2025-10-01 04:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0c114946-0c89-3cc9-8086-8f7b1deb280b | -2.63395 | -48.04186 | 2025-10-01 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89d518d2-a894-38a7-9063-56bfbd549f74 | -5.63586 | -43.91141 | 2025-10-01 04:49:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 63ca3d64-a085-35d6-a337-665f0dc31e26 | -3.46663 | -50.0948 | 2025-10-01 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| fcec61f4-34e9-3f08-9469-7a4daf5409c7 | -8.64861 | -46.61876 | 2025-10-01 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| aeb95cbf-43f9-37d3-b54e-48639d32b9ab | -5.47412 | -43.07924 | 2025-10-01 04:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4aefd006-204a-30b5-8274-ab013bbce7ab | -3.09087 | -48.48882 | 2025-10-01 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b6cffa3b-966c-301b-82e7-acd963886315 | -8.72196 | -47.98502 | 2025-10-01 04:49:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5bbbf116-631c-3f6e-8f94-c1766fd7a180 | -7.05389 | -46.41068 | 2025-10-01 04:49:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bdb870c9-5a97-3436-9e4c-41b4589e893a | -8.28921 | -50.80052 | 2025-10-01 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1630ccce-d951-3d2c-988c-5f48bd279b8f | -6.66394 | -41.39984 | 2025-10-01 04:49:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 75081935-e140-3ba0-92f3-39786adf9953 | -5.53438 | -43.87023 | 2025-10-01 04:49:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| de6f330d-8090-3376-8053-ccfd83c2e2c8 | -3.21928 | -47.63113 | 2025-10-01 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e33407ba-830b-3b25-81a3-7e4b9f273476 | -4.26317 | -48.55409 | 2025-10-01 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04d73f9e-a755-3f2d-b581-b3c71ea64c51 | -8.55368 | -44.75095 | 2025-10-01 04:49:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad72d37d-78dc-3dd7-b87f-4ab10c132aa1 | -7.47856 | -46.47266 | 2025-10-01 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d3c29718-f1a1-39ce-9955-f222af4cf4df | -5.95726 | -45.87151 | 2025-10-01 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b9ab8290-daf9-3c04-ae5c-8a432248ee82 | -5.20922 | -45.6732 | 2025-10-01 04:49:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 75c1fce6-6f0d-3c9b-958b-1dc1d7884417 | -7.02113 | -44.48715 | 2025-10-01 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8097e30-921c-38fa-a5ee-149177266844 | -7.02432 | -44.78886 | 2025-10-01 04:49:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f58b08b-51b2-375e-aa77-8a20961879d5 | -6.2096 | -44.23136 | 2025-10-01 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1188e739-2a7d-36e9-8abe-209cc4a60c98 | -8.86461 | -47.64319 | 2025-10-01 04:49:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 457a46f0-f078-35d8-980a-6f637238efcc | -7.82484 | -47.06321 | 2025-10-01 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6cc58a0f-2dea-3d45-a808-62985ea5f68c | -5.77503 | -43.2868 | 2025-10-01 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ab441ae-7788-3ee0-b0aa-e753a5d34ac1 | -4.63764 | -47.02092 | 2025-10-01 04:49:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 08ab1873-a2c0-33a1-927a-b4f829f99459 | -6.28125 | -43.65104 | 2025-10-01 04:49:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0149911d-6c50-3c61-9214-f89dcc9a5c53 | -6.67963 | -42.80562 | 2025-10-01 04:49:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| e8fa548d-3f24-3c56-87d2-eb5d2002c773 | -5.62614 | -51.94123 | 2025-10-01 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a3784a2-5d0b-32dd-bc9b-061b8bbb9739 | -7.82568 | -47.06019 | 2025-10-01 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 94f028d7-398b-31f3-88a1-3f369b8fb687 | -4.23078 | -48.15225 | 2025-10-01 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 56362eea-b8cf-3ce7-8852-f3df78e84e41 | -5.90401 | -43.93262 | 2025-10-01 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ac75ea7a-c200-3c80-8147-6ab9a849afa4 | -8.53863 | -44.69201 | 2025-10-01 04:49:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4df122da-2d47-3eeb-a15b-24fbe893ec84 | -6.03575 | -43.81073 | 2025-10-01 04:49:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 20fd9b70-2c51-3149-801f-8c7b7802d8b9 | -7.84509 | -47.06293 | 2025-10-01 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c11bda2-c66f-3557-a7cc-2f7cd518d164 | -6.39234 | -44.28732 | 2025-10-01 04:49:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c923a36f-041a-36d5-a4fc-a7b773ab691d | -5.64586 | -43.9077 | 2025-10-01 04:49:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 77f19deb-83ba-3448-b74a-66b550e52659 | -6.61498 | -44.26294 | 2025-10-01 04:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 240dd881-074a-3a2e-9c40-4d2513ad365d | -6.90254 | -44.9809 | 2025-10-01 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a8a4806e-4794-3c43-8eef-1c8469f86ec6 | -8.55372 | -44.65106 | 2025-10-01 04:49:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a77eeeb9-9d5d-3fba-ae12-0d0944298b2f | -8.58902 | -44.73188 | 2025-10-01 04:49:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61163205-33e3-3495-bfda-a10f009e2254 | -8.5393 | -44.68724 | 2025-10-01 04:49:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 005457f5-fea2-3076-8c59-a9b6e4b631e2 | -3.46717 | -50.09134 | 2025-10-01 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 56bfdf99-b61c-3ac8-88ce-e824cec19b20 | -3.45664 | -50.09324 | 2025-10-01 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e61d2c4a-6722-379a-95fb-64bf5d153a15 | -6.49069 | -44.28676 | 2025-10-01 04:49:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 206c844f-109d-30bf-82d7-e245079aa8d8 | -3.26969 | -52.50823 | 2025-10-01 04:49:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 61552ab0-a27d-3292-82d1-e41ac3ceda94 | -6.80272 | -44.74441 | 2025-10-01 04:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f19bedd5-ae1a-30e8-9988-dd7f11cfad4d | -5.76514 | -42.8664 | 2025-10-01 04:49:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 5f93c126-6440-322e-83ec-149370814ec1 | -7.08901 | -49.17662 | 2025-10-01 04:49:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0c4120bf-3b71-3965-b767-d78a768e9d26 | -6.72967 | -49.6344 | 2025-10-01 04:49:00 | NPP-375D | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95e5e0af-c8fc-34a8-9d16-1962599d9bf9 | -3.41832 | -51.22831 | 2025-10-01 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 87a41b05-af53-3e54-972d-680857c73fe3 | -6.05285 | -44.43863 | 2025-10-01 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6c51ffdf-2db2-370e-8039-53387ec4b007 | -8.58051 | -44.75871 | 2025-10-01 04:49:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c29f36fb-cece-39e4-81de-ece61f99f0d7 | -3.46827 | -50.08442 | 2025-10-01 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2f4db0fd-b6de-3323-bcf3-e8d943d907ba | -3.0943 | -47.01579 | 2025-10-01 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 4fa004f2-6752-3343-be8b-70a4b6534250 | -3.51813 | -49.44204 | 2025-10-01 04:49:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8cbb8fc9-ae9e-3f03-8086-d8e16c0b819e | -8.89037 | -46.63928 | 2025-10-01 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aee92452-e327-30e2-85b5-d2de8cc0d3d2 | -6.9948 | -42.80166 | 2025-10-01 04:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e92738b8-3ae5-3fd2-9acc-13d902853691 | -8.16657 | -46.24485 | 2025-10-01 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d46dd6a0-907f-38dd-9fa3-ac2d25df288b | -7.02427 | -44.46466 | 2025-10-01 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 03ba547e-436a-3c5c-b784-156ba570fb49 | -6.02357 | -43.78189 | 2025-10-01 04:49:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f81e0d28-409e-365c-a519-9e74b03ce56e | -7.82816 | -47.07049 | 2025-10-01 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a1aee94-b104-3322-b98e-b0b17e7b50ac | -3.09376 | -47.01387 | 2025-10-01 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 957a0a0a-ecba-3299-bc21-bfadfa42123a | -6.28535 | -43.65992 | 2025-10-01 04:49:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c2d6a48d-88a4-32e7-8257-98640d495c19 | -7.6304 | -45.45228 | 2025-10-01 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 247198f3-77a7-3f78-8f4a-06670fb75f68 | -5.41364 | -41.32975 | 2025-10-01 04:49:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 32fe142d-1bc6-39a9-b0f4-fa65c0c0f539 | -6.11502 | -43.48843 | 2025-10-01 04:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f9365da0-ff30-3a5f-9eaf-e5acc57b9b42 | -7.41938 | -45.4085 | 2025-10-01 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6053ae4b-6ebb-3e75-a656-6d44eddba60a | -4.04069 | -54.13811 | 2025-10-01 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c805d2e-8243-3fca-b7ff-def29f6e320f | -4.25742 | -48.55406 | 2025-10-01 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8816028-537b-322e-9400-9ff64ebef313 | -4.98052 | -50.63764 | 2025-10-01 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 74efb6ad-4141-348a-b8fa-3f0245391056 | -6.64315 | -42.03443 | 2025-10-01 04:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 968b5ca0-35f6-3920-81b3-eb3cd7eff6c1 | -3.33015 | -50.25061 | 2025-10-01 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ee62e35-7284-3960-a4e8-9efc67520b8d | -5.6267 | -51.93768 | 2025-10-01 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 605c67b5-a441-3d1c-8d21-0d1531c1cfd0 | -6.03564 | -51.89361 | 2025-10-01 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5fbbf7b3-f414-3ad6-a165-651154fc8a25 | -3.89494 | -49.08471 | 2025-10-01 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 110c1c7a-9517-3376-abc6-9a81e2358a94 | -7.37979 | -44.03383 | 2025-10-01 04:49:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 324688e0-0707-3f6c-8b91-fb1b98de1c4b | -6.03869 | -43.80945 | 2025-10-01 04:49:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85abb5ee-01f7-31fb-aa6a-4f6e0b93618f | -6.20986 | -44.22792 | 2025-10-01 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8f4b43cc-5f6d-3aa9-bdd4-6adaae553e8b | -2.59339 | -48.12058 | 2025-10-01 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 9446c5ff-02d3-39c6-b6f5-b50510777aaf | -5.94115 | -45.89743 | 2025-10-01 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b1a79cf6-f6f6-3dcd-8428-bd927c6388f4 | -8.89931 | -45.04652 | 2025-10-01 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 279eb835-ffb6-32ce-ad65-9e8eb03dff2b | -3.89601 | -47.17696 | 2025-10-01 04:49:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51c5ef35-4e49-368b-9b13-a8ee99c16163 | -7.1358 | -47.28847 | 2025-10-01 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 60a9609c-8a5c-32dc-9ed2-7c247ee60c64 | -8.87601 | -47.64482 | 2025-10-01 04:49:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 997f5146-9a95-312a-a892-919fa61f047f | -5.85429 | -43.40703 | 2025-10-01 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d7e25de1-a309-3383-8d6e-2553324bb4f9 | -6.81429 | -47.3242 | 2025-10-01 04:49:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 3d03b479-e515-3d3b-b1cc-b6d265d3e194 | -3.08425 | -52.92313 | 2025-10-01 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 49ba078a-da80-36a1-b9b1-79cbf2b00d41 | -6.45721 | -43.94386 | 2025-10-01 04:49:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f3a05e60-99b8-3be3-9006-46fd56845828 | -3.25558 | -50.11854 | 2025-10-01 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b79f34a-be57-354f-ae84-2ccd942d6166 | -5.17958 | -41.24146 | 2025-10-01 04:49:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 54ac1c9b-4de1-3b8e-b25c-42ec7396af1a | -7.8433 | -47.04792 | 2025-10-01 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README83.md)
