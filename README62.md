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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8f9168e-6b38-3f75-abc0-f35f608708c1 | -3.33868 | -59.80378 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a784ed92-2dbc-3b78-88b7-0c0a6f638452 | -6.09531 | -55.56602 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 460caa50-e546-30f5-8fe0-e9fbf052ee73 | -2.94925 | -51.03807 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 51751d96-1113-366a-8167-532b0d8b882c | -2.98171 | -54.76404 | 2026-09-21 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a87c237-55c0-3038-ae89-4df01cf506fa | -6.72477 | -55.07981 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 34b575d7-8d27-386e-b27d-f2fea850bf64 | -3.34709 | -59.85049 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 23858443-23c5-3e1c-96b8-abca3594305e | -3.53747 | -58.69565 | 2026-09-21 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| db368797-c4af-3480-aa66-5b786cb6d8e7 | -3.40846 | -50.751 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b141dbe6-c98f-3980-88ec-99dc3e2070fb | -3.6186 | -52.18795 | 2026-09-21 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b01ecf66-9ae6-3b7f-a223-e492b9232a77 | -7.38999 | -51.77579 | 2026-09-21 05:04:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 22cbd489-d143-3fbc-8663-4bf2cb4c21fe | -6.19942 | -57.77615 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5408eab1-2547-3843-96a4-592386be6bfb | -6.16226 | -57.72493 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bbf6e4b6-21c2-3966-8b6c-d8ecbc53df4b | -6.73538 | -55.09943 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0896c68e-5ce7-316c-8fef-2db111647a45 | -4.356 | -55.65921 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bbf2f970-5a68-3d01-aabf-8fce357e1579 | -4.15794 | -50.23722 | 2026-09-21 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a0e1b86-1927-30f0-9114-7c8412e59a4d | -3.40447 | -61.34396 | 2026-09-21 05:04:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 40db5a04-74bc-331a-b7a0-60318d801b3e | -1.20201 | -54.22218 | 2026-09-21 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbcf6783-6552-32c6-a375-faca87ec6677 | -5.81257 | -57.73399 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9413147b-ce3e-36f0-8b58-2256ae3296ef | -6.02129 | -55.342 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad8041e7-7433-3fed-9b88-abbce1ffbb17 | 0.78556 | -59.20542 | 2026-09-21 05:04:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6067cebc-3405-3d94-82c1-6b063904fdde | -5.89209 | -53.64196 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 31f95bf0-ce50-300d-8504-785d3f73086b | -4.22602 | -56.40096 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d83b93c6-e8bf-3f8d-87f6-b5cb1686418a | -5.2015 | -56.10316 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df0c141a-83e0-3bd8-a795-91c48ae8d1cb | -5.82112 | -53.51035 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4524ae9-004d-3361-a3b8-e92aadf527bd | -3.3033 | -57.86609 | 2026-09-21 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7ce3ba31-b0a9-3152-ae24-77191bddb9ca | -3.00714 | -54.16394 | 2026-09-21 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db65a476-277c-34b2-923c-7d1b50527918 | -6.16106 | -57.73232 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dbde1b21-0ab1-3d8a-a2ed-5329a19775c3 | -6.42192 | -55.01497 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cd7d9050-1435-3484-8e5e-b53fba20af7e | -3.38238 | -50.44191 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 1e5e64c3-b771-337f-9b5d-a41e16874be9 | -6.72531 | -55.0763 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c53cb4b-ce46-3a83-81da-621ed286070e | -6.28839 | -57.74848 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 91b36a84-d3f8-3706-ade4-2352d4ee8f48 | -5.95241 | -52.22739 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 292f74fa-8c86-3d5a-92ea-ed52e9f0a448 | -4.36197 | -55.36098 | 2026-09-21 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fea71844-5f18-31e8-bb47-2a95ac87bf56 | -6.72702 | -55.08737 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 15235efb-7b0d-3a5b-91bc-1875b93b8ef8 | -6.39846 | -55.25495 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c95ef1a-782e-347c-ba0c-fb3c352a1577 | -3.43853 | -58.02266 | 2026-09-21 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fd64b10f-0817-34c3-9bcb-4641cfabae99 | -3.33084 | -58.1294 | 2026-09-21 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2f5b63a-a38a-3afc-8f0d-e57a7a85d697 | -2.6425 | -54.69341 | 2026-09-21 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5e12d17e-17da-3f54-9e9a-7500b5b3de78 | -6.09829 | -57.68427 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 73b24bd5-504e-3afa-8ddf-e20c22cc7bbe | -5.8454 | -53.50579 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3cc3017-f8fe-32e8-bfe0-0cde6ab173a0 | -3.34467 | -59.86539 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f0afcc0f-25e8-3545-b177-9c4ef8b4e69c | -3.83786 | -56.98736 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| de5dc858-c050-35cb-9b0a-b12ffb6852f5 | -5.87887 | -53.63599 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b1fa77e1-c55c-3289-aad0-daf1fee14530 | -5.83909 | -53.54796 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 054eef3a-9a16-33a0-abc8-3016d70baacf | -6.09489 | -57.68371 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8961570b-b523-3824-a591-04063ce4e777 | -6.30035 | -59.93684 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 24acc538-b5c3-3a1f-aa92-d8e3f48ad80e | -5.98051 | -57.78315 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd71b2c5-d8d4-34bc-a97a-43f9d4400eb9 | -5.87207 | -52.06348 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e15f7212-1a48-37bc-8704-390a28e58e5b | -8.371 | -45.63194 | 2026-09-21 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e1640d50-13ae-3614-b6e2-f2528a907306 | -8.37047 | -45.63614 | 2026-09-21 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6308e2be-74a5-31f5-9597-40de4ee51d0c | -6.73026 | -55.06624 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa00b87d-f380-3720-9af9-5e0644b3e6a1 | -4.34886 | -55.66163 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b07a2d9-a0c1-3126-bdad-ae3430a655fe | -4.2607 | -55.76757 | 2026-09-21 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93c768cd-094f-3e2c-b3ed-8cbf02fd6e0e | -5.89787 | -52.09492 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1df1163c-e731-3e75-99e6-bd751daea592 | -2.87593 | -57.81728 | 2026-09-21 05:04:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 20ad2433-c902-3715-b911-db0304cf893b | -2.87594 | -57.82126 | 2026-09-21 05:04:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2a889e87-1a2e-312a-825a-e18501b004ee | -3.48289 | -59.56184 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7514346a-154b-3e47-a282-6e9d186c1e46 | -2.91119 | -54.18866 | 2026-09-21 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 169ae228-d295-3be2-bba3-020c62a6e124 | -5.81648 | -53.51749 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72836257-99d6-3c47-8071-e930a2f91189 | -3.00992 | -54.16797 | 2026-09-21 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4363f5df-cb01-3474-b997-dd3e6969b167 | -4.15933 | -59.92633 | 2026-09-21 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2786e772-12e1-36fc-af33-0ec2412467b3 | -2.58791 | -59.99307 | 2026-09-21 05:04:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 540484b4-ae35-3c40-98ea-4482bafe77c9 | -6.16063 | -57.95267 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dafa66d1-fefa-3b8d-95e7-f9cbd071e7f9 | -6.72594 | -55.09436 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33f5d0ad-5198-3bba-b5bc-ea82a456c6e3 | -6.73034 | -55.08789 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44b4153e-12c7-3ffc-b0cf-5024783f6331 | -6.46959 | -48.44216 | 2026-09-21 05:04:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9dc08687-447f-3e3d-a09e-f3632825c251 | -4.0443 | -55.71566 | 2026-09-21 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa1ce906-7c93-3df8-a352-41a32d5d7f1f | -4.35546 | -55.66265 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d258685-a946-3db2-8b68-955889711d3e | -3.43106 | -59.26048 | 2026-09-21 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 2b686a02-ab4d-3204-8af4-1ca43776559e | -6.83884 | -55.74985 | 2026-09-21 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e9db76f-767c-3924-9b74-56f4887c1a79 | -3.39804 | -59.58487 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b0a7fb0a-e015-30ee-b83a-c3629a68fc8a | -6.21044 | -57.72898 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e461e97-2a59-36a7-8e9f-0a9f2a5e2362 | -5.20042 | -56.11006 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f3c8219-19b6-38c7-9390-01ba9aa8fc07 | -2.87242 | -57.81673 | 2026-09-21 05:04:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0e8ed3d5-3e56-3165-9249-8cd6e3fb7deb | -6.90904 | -43.73311 | 2026-09-21 05:04:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 935974d2-166d-38d4-8725-7dc85f58bf51 | -5.87093 | -52.04543 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e6479b6-1234-3af7-841c-2e4f65ba7f8c | -3.05146 | -61.26904 | 2026-09-21 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 698268cc-16d8-337e-9f35-32e348fbcad3 | -5.80927 | -52.08837 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 79e24a2a-6250-30f6-8be9-740cbd2092d4 | -2.91452 | -54.18917 | 2026-09-21 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09ef7826-0248-3305-8de8-e92b75b1c095 | -3.17925 | -58.5881 | 2026-09-21 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4403e966-d025-322d-8e6c-b34361d2c1e0 | -5.01387 | -56.08741 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a6f7b76-673e-3825-8dfe-1c0be7e78412 | -2.92023 | -57.79199 | 2026-09-21 05:04:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e67e3877-54a9-3695-bb7f-a5eea95d9a61 | -4.22665 | -48.61303 | 2026-09-21 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 74a646f6-04ba-3f27-a6bb-7222942d5715 | -6.311 | -60.01438 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 61f18931-aa2d-3a6b-9005-80b84177d02f | -5.9864 | -55.69734 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d4d9ef1c-9bc1-3fe0-9a76-0a8ff5c57429 | -3.48744 | -59.6064 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c44adc5f-e9cc-301b-9393-6f646efd0122 | -4.80802 | -56.07644 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e839c1bc-935f-34a8-9e3c-ae8b1188539c | -5.84716 | -53.54138 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 41f2e006-917f-3daa-8474-f93549d08dd4 | -3.55048 | -58.75455 | 2026-09-21 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e82713f2-8153-33ce-b574-a1cd2bd41379 | -3.36993 | -50.44356 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1408094c-da49-3836-94f4-a6e60d978d08 | -6.35411 | -57.77388 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e438797a-d2d5-3ebe-b68b-51c3ace38fea | -5.9028 | -55.7302 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8519b505-cf50-3033-8d77-8f73a340fe4f | -3.47669 | -59.59984 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32de6df3-5a20-3169-a934-2b7061e57e8f | -6.75407 | -55.61623 | 2026-09-21 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1dd6e0a-cbe2-3994-a277-805e2f0a6a7f | -6.13928 | -57.77761 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50e9ba69-3e5a-3117-b3c7-98762d2cceef | -6.73584 | -55.07436 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c8e5d7c-6873-3075-b8b7-46fc6ad8fd7c | -6.83028 | -55.54275 | 2026-09-21 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7472ef8-2ce9-3a3c-a5cf-312f9a760ccd | -6.1101 | -55.68845 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b448df7f-89f4-3506-aaf2-e0437aa75ad4 | -5.80916 | -57.7334 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f91b566f-d415-359b-a5e3-25ecf1585a42 | -6.89356 | -55.65911 | 2026-09-21 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README63.md)
