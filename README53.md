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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97195b7b-5707-3f83-a0ed-43eba530d428 | -13.55282 | -47.28447 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c78bd544-43b6-3b04-ab0d-96170e988237 | -16.00265 | -50.89644 | 2025-10-02 04:04:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f6a34f96-edc2-3080-b2c0-8a847662007c | -14.90907 | -47.22932 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ae1673b-7a71-3333-b78f-47aa401452d1 | -14.36852 | -47.12973 | 2025-10-02 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7470e817-e25f-3cb7-b85a-338123e98887 | -14.98902 | -46.90406 | 2025-10-02 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 450e442d-9813-39ff-9932-09c02283bdfb | -12.76262 | -50.55418 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c3c6139f-6245-32ec-bb01-d021cca44485 | -20.12726 | -46.32801 | 2025-10-02 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17857805-2df9-3797-aa12-90b605452e1a | -14.69651 | -49.62172 | 2025-10-02 04:04:00 | NOAA-21 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ae0b10ed-618f-37aa-a48d-604bf15007e3 | -15.99984 | -50.91055 | 2025-10-02 04:04:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| dae3f70e-7518-3d93-b9e8-b6df1484c93f | -15.39989 | -47.04593 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7ed62e83-7d7b-365e-b0b2-c7f2af8f193f | -14.90278 | -47.21311 | 2025-10-02 04:04:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a28b9fc5-5dec-32a3-ac8b-bfc92907a693 | -13.76213 | -48.69292 | 2025-10-02 04:04:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ba6a68ed-b815-39d0-8cae-4e0e49e4a488 | -16.04231 | -50.85407 | 2025-10-02 04:04:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4a133dce-e31d-3bcf-a980-74a5478f4b6e | -14.18922 | -46.12659 | 2025-10-02 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 96ab4105-cc92-309f-9406-0114572f294f | -14.90462 | -48.31775 | 2025-10-02 04:04:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 078f9146-cf45-3590-8142-de075d91e16e | -17.87303 | -42.26185 | 2025-10-02 04:04:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 38e3539c-f63a-3fd5-837b-dc8654ab87a9 | -15.70127 | -46.25672 | 2025-10-02 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 716e99d3-309b-3a80-ad86-3ecb8f96251d | -13.80142 | -47.52869 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 00be3216-3a0d-39bb-9cac-0ee0c9c7fcaf | -20.44598 | -45.35797 | 2025-10-02 04:04:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8b538f6f-a356-3200-9893-81a69cc3ad9a | -13.35671 | -48.12061 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 00892627-a2e2-3b80-82ba-f9695aef6d3a | -13.30857 | -47.57816 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3ae3b773-36ec-3ca1-b9a3-db5103a1b998 | -14.30697 | -45.98758 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 57da3787-1cb1-3fd4-8aad-effc5d83abea | -14.87424 | -48.28862 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a2b3912-f83c-336f-a4f1-798ba468414b | -12.47775 | -54.42567 | 2025-10-02 04:04:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b7ed6025-878b-3b06-9c51-794a202eca96 | -13.52687 | -47.26253 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eb0fb2a7-569a-3abc-938c-2179a88d06c9 | -15.27925 | -46.39991 | 2025-10-02 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dc389586-c756-3a1d-9c44-7925904de9d7 | -13.31818 | -46.99996 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b95c0d42-4115-35f6-bd5f-975b26cc9a04 | -13.05832 | -47.00204 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17bb61e7-517a-3bd9-95e0-2588c1f50647 | -13.69776 | -48.62946 | 2025-10-02 04:04:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 70b19b3f-eab1-38d9-ba0b-73950ccb6faf | -19.05054 | -48.1383 | 2025-10-02 04:04:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2b7ffe25-0c46-3595-9cd1-6ecc111d0529 | -14.70274 | -49.62058 | 2025-10-02 04:04:00 | NOAA-21 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 35f520f4-4e06-3bf0-8502-2e2749689142 | -12.67622 | -48.57052 | 2025-10-02 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d092cf8f-cef9-3b13-b67b-b7984be7b9d0 | -14.2861 | -45.97338 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fadaa2c7-ad89-37c6-95fd-7a67618383be | -14.85581 | -48.29155 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 916b8395-5bb9-3179-afe1-7967cca9a267 | -12.58079 | -49.89698 | 2025-10-02 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0a4d020-519c-37c9-8ebd-d3be023e1ddc | -14.58191 | -48.31971 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f5a18155-a16e-321c-b89d-58d1cb87aa8d | -13.76309 | -47.98148 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b5b9915a-02d4-3bf9-88fe-fc019df90c69 | -14.31452 | -45.98899 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 63dfa3db-b5e3-3868-bc1a-f565bbb53806 | -13.96174 | -48.11213 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 046f72af-3ee6-346c-847b-104961a65e22 | -13.14921 | -47.78667 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37387a59-81d7-367f-92f9-b72129b5a7f2 | -15.6055 | -46.91503 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02fdf64e-3d94-3287-84d8-a64660a5667a | -13.2207 | -48.44176 | 2025-10-02 04:04:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 53bb9862-20a9-3777-8312-29680dac6002 | -13.40104 | -47.54839 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d1631aff-9781-3ee9-a678-e4b04daaa261 | -14.30571 | -45.97253 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 075f42a9-ee76-316a-aaef-0ca14df48e9e | -15.86326 | -48.13209 | 2025-10-02 04:04:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 88104bac-6961-3338-9314-9f7a728bb96b | -14.5827 | -48.3154 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 36fa6724-948d-3813-b68f-cfcd285bb2f9 | -19.51503 | -43.61475 | 2025-10-02 04:04:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8b968222-9c49-387d-bb04-47ec531fa608 | -14.48396 | -48.40939 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 85fd02d2-306a-3aab-b590-e453790255df | -13.80762 | -47.54221 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 88fbf9c2-43d5-3686-bac9-08a1e4ddca1f | -14.37262 | -45.96865 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c66506c-e0ac-3244-ad52-19f8380f6ea9 | -13.37549 | -47.28393 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ea118c2a-98ea-38fc-b646-aabbfb5e5ddf | -14.36552 | -45.96398 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 25316ef7-3292-360a-ad54-9caa2e934ce5 | -13.28605 | -47.24653 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 539c78c1-7102-3ab2-bbce-596e2c3c1328 | -15.29948 | -46.39114 | 2025-10-02 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac1d1f19-e49c-3183-8820-954ae87422b5 | -13.07667 | -46.99385 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b703152b-7b63-326a-8b47-c2b97b13544f | -14.6558 | -48.12264 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1f698ffc-e583-3050-89cb-e3949ffbda8f | -12.7098 | -48.59412 | 2025-10-02 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 451d1edd-52e4-3ef2-9272-fe7147ac7af0 | -17.91138 | -44.60683 | 2025-10-02 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8f961c31-3854-38ca-9c86-ad616ccd1b59 | -14.98323 | -46.91357 | 2025-10-02 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| db2f1bf1-42a8-3aef-80a1-6a5c6e685617 | -15.31928 | -46.27995 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e19681f3-8c8c-3aa3-ac8f-b5c542495452 | -13.4203 | -47.80009 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 044eaaf3-0c2f-34b2-8b10-63fd12a9970a | -15.35261 | -47.08875 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 342cb238-9309-3418-b41f-b6c08600f3c4 | -17.96474 | -45.0437 | 2025-10-02 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 993c5c13-7117-3b5d-a254-12e1f886d8cd | -17.95228 | -45.03325 | 2025-10-02 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f803e3d-f99e-3b1d-870f-31edf18f764f | -12.50106 | -50.25451 | 2025-10-02 04:04:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 67744be7-708f-3c90-a56a-6955c5a099f2 | -16.02993 | -50.86408 | 2025-10-02 04:04:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80d12d28-e176-397c-9de7-d8ad7dd6d4bf | -19.5201 | -43.60427 | 2025-10-02 04:04:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1ccb2f26-eea3-3a52-a93a-c6389a0eaa27 | -16.36835 | -47.05733 | 2025-10-02 04:04:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| df0e955b-391f-3213-a2a0-d2f812fac063 | -15.59861 | -46.90828 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e1be7864-76bb-38fc-b5a3-51f53b2b41ba | -14.92652 | -47.22503 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e0f22f7f-5b5d-3e1d-8018-adcd7764ba7b | -13.787 | -48.05483 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 13567d72-7b88-382a-974b-fcf20bf31c7c | -18.86115 | -43.25396 | 2025-10-02 04:04:00 | NOAA-21 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d8b2123d-8492-31ea-8c64-9f0bf8c96085 | -19.78023 | -42.41618 | 2025-10-02 04:04:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1b9c1327-c28b-33ea-8d8e-c819f616601a | -15.94892 | -43.32289 | 2025-10-02 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e33a589a-6316-3aba-af25-0aa8d7d99f69 | -13.78643 | -48.00051 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8ea8ab19-2109-3832-badb-cfb53ab37e1f | -15.28155 | -46.40335 | 2025-10-02 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2f5111a7-97a4-3f25-8ae3-d9f55428602a | -14.40163 | -46.09181 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 118a7cd8-6f67-3d27-80b1-0ec50d39260d | -14.47885 | -48.41241 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 239315a9-b4d5-3f4d-a542-8165de72ea05 | -13.40898 | -47.78935 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| eeef7198-6dab-3157-9825-f49b243666dc | -14.34531 | -43.83762 | 2025-10-02 04:04:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| edd4f03a-4570-3a46-b548-4aff244125da | -16.03727 | -50.85326 | 2025-10-02 04:04:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c47a5644-7e8a-3100-9d48-2670b7de758a | -12.69373 | -48.57829 | 2025-10-02 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| caa64a14-0852-3f77-86a6-a56c8a4a6d16 | -12.5009 | -50.24371 | 2025-10-02 04:04:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7850bd63-0676-3b25-a362-ebfa24b875d4 | -13.78414 | -47.99829 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 69f177c1-a278-3389-b3ec-41d8794f2355 | -18.43319 | -46.53476 | 2025-10-02 04:04:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 512e101e-5a94-32e4-b673-d97a1c9ded91 | -12.70653 | -48.58595 | 2025-10-02 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d6833048-9436-335f-b6b1-18303b822713 | -15.34398 | -46.29496 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ab955ee3-8c04-3afe-aecc-e20edf0c5f05 | -14.4303 | -46.10699 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f09f5054-805d-3b5f-a989-8c3dc04d578e | -14.35556 | -43.83938 | 2025-10-02 04:04:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef267edc-d2c9-3efe-b583-674883288db8 | -18.13715 | -42.40231 | 2025-10-02 04:04:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5fec74bb-4dd8-3473-b686-898c590e6abb | -17.08389 | -48.56163 | 2025-10-02 04:04:00 | NOAA-21 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ab3e6063-e0ab-3db3-8364-d882264eaf04 | -12.762 | -50.55743 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 2f6e228e-a1f6-36ba-8a7f-5219be3b1fad | -15.7581 | -43.67649 | 2025-10-02 04:04:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6de7ae6a-ebab-3b19-8dc0-23ee686fe260 | -16.04833 | -50.87632 | 2025-10-02 04:04:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ff62b67-467d-3b59-94be-151937391c49 | -13.75954 | -47.9519 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 33e9744d-9396-3eed-a41b-47719f289930 | -13.22681 | -46.433 | 2025-10-02 04:04:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e65ab21-ceed-33c4-aab5-67ecd3ca490d | -18.50129 | -43.39632 | 2025-10-02 04:04:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c2c28c55-91a3-3939-b49a-96db80b74029 | -13.65802 | -47.30584 | 2025-10-02 04:04:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4c1f6a7a-e0f3-3134-a60c-5211dfa808ea | -14.41516 | -46.104 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 76644406-78ad-3a08-ab6b-cb08ffb4193e | -13.07601 | -46.9976 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README54.md)
