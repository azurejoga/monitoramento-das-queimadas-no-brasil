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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8685425a-677e-3fa9-b462-6f3191b7449c | -16.81376 | -48.80995 | 2025-09-27 04:25:00 | NPP-375D | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4bf2745b-48de-341a-9a6d-a3f8893d3606 | -15.9047 | -57.4964 | 2025-09-27 04:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 00a1c717-11db-3897-8182-47d39b5a8b3e | -15.03719 | -46.95625 | 2025-09-27 04:25:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 66609246-a9a3-3dd2-af3f-a8ddcbea7c18 | -12.48491 | -54.32102 | 2025-09-27 04:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 326a2006-ed45-30c9-a501-edab752de79f | -17.34025 | -44.46087 | 2025-09-27 04:25:00 | NPP-375D | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 84234f1d-a17b-311a-9cea-d2041ebaa40b | -15.55979 | -47.91614 | 2025-09-27 04:25:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5328c06b-f580-31ee-bf47-d6868123e1de | -15.27487 | -46.45923 | 2025-09-27 04:25:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8dd071e5-d131-329a-b4d7-7c54bb28c581 | -15.9133 | -59.32886 | 2025-09-27 04:25:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 24acc315-75d4-32e0-849e-0f1aaf633c37 | -16.45032 | -49.08347 | 2025-09-27 04:25:00 | NPP-375D | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc86b6e6-bb38-3849-98af-406df5ed6cb7 | -15.26411 | -51.47791 | 2025-09-27 04:25:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7856e8e0-10f4-33d8-aa5b-0823b87c296e | -14.84581 | -45.609 | 2025-09-27 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b01d781-c40a-3a92-b7f9-ffd400b9ad23 | -14.95 | -47.49928 | 2025-09-27 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4295c41-6da9-35d9-98eb-d7a00ac6733b | -14.94666 | -47.49869 | 2025-09-27 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e3b2f73-114b-3f9f-9b38-68ad079804b3 | -20.27831 | -46.00872 | 2025-09-27 04:25:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| dd2bc56d-712b-38c6-83d5-08dc94b54643 | -13.60466 | -47.30336 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 869e7e1d-cc9c-379c-b27a-5fdac2418304 | -17.73409 | -46.70792 | 2025-09-27 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 86ecc76e-e21e-3f77-b95a-b0b97fa7c6cc | -13.52033 | -47.41247 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e83de1b6-aed2-3202-a614-0d72bd287b3f | -13.60962 | -47.3153 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dee14deb-b425-3709-a74c-db58ec88b9d1 | -15.53429 | -44.33051 | 2025-09-27 04:25:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a4398415-cfff-32c0-a1f5-ec56e9ee58cd | -15.14521 | -46.42343 | 2025-09-27 04:25:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 282e6cc3-2e10-3526-8d2e-33fa2c2430d3 | -14.77279 | -60.18615 | 2025-09-27 04:25:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c025d216-8442-3dc2-a45b-bc198025f222 | -13.61691 | -47.31274 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ffa7d993-9379-3773-9ae7-bf2529b1d368 | -18.18369 | -53.34201 | 2025-09-27 04:25:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 84fe7135-996f-376d-b44e-4cf62d9c0fb6 | -14.0625 | -48.8262 | 2025-09-27 04:25:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8c8a04a-7f33-32f2-aab5-d80e66f7e9b4 | -15.5509 | -47.9071 | 2025-09-27 04:25:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 071c172f-0c32-34ec-9318-724430a2c9b9 | -16.76173 | -53.35761 | 2025-09-27 04:25:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9f3b6846-a4f7-36f0-9b6f-fe68f15b218e | -15.42994 | -48.21676 | 2025-09-27 04:25:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90f56a16-0cf1-3dc6-8b3e-ca630f70632a | -15.7566 | -48.50344 | 2025-09-27 04:25:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 562b14e3-72be-38b2-9c79-c7bcce79fdc9 | -17.11642 | -46.87001 | 2025-09-27 04:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| df743ae8-ed2b-303b-8e30-c0e9916d5d58 | -14.51603 | -48.01624 | 2025-09-27 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 23eaa5ea-4d95-30db-af83-319f7c23b2f7 | -13.32928 | -48.56239 | 2025-09-27 04:25:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b16165f2-e3ab-32c0-a0df-d89a8b0fc12d | -15.53956 | -44.34365 | 2025-09-27 04:25:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d6821a00-52f8-3965-baa7-b5b69e39af5c | -15.32533 | -47.87672 | 2025-09-27 04:25:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 71f3dc6b-0aa3-3fe0-8b95-29401d970760 | -13.6243 | -48.08526 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5a34a040-ae19-392e-8b59-7501369efd0f | -13.67467 | -50.63792 | 2025-09-27 04:25:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| edd6585e-f15d-3564-8514-13307bc4525f | -14.77299 | -60.18557 | 2025-09-27 04:25:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 51d28307-56c6-3f52-b62d-334c2f0fa72b | -18.29829 | -57.09233 | 2025-09-27 04:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| ab86079f-26d5-3969-ac69-56a5489a2eb1 | -18.3204 | -57.11931 | 2025-09-27 04:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 83803ae5-5220-3161-a0d2-b220eedb4935 | -15.5687 | -51.70855 | 2025-09-27 04:25:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1acb53fd-5cf6-375b-995d-5e0e6a1e48b2 | -16.15984 | -48.09438 | 2025-09-27 04:25:00 | NPP-375D | NOVO GAMA | GOIÁS | Brasil | 5215231 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 59879dd4-f140-3eaa-8cad-ed29cc5b1fe4 | -13.83407 | -47.95584 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0534582c-6d2b-3d7d-b422-2c399c839e33 | -15.2013 | -48.45902 | 2025-09-27 04:25:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1a47ee67-e059-3838-a610-5bf3a292db9d | -19.311 | -48.90754 | 2025-09-27 04:25:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8ee842f-06de-3684-9313-a17993c923bb | -22.59884 | -48.57787 | 2025-09-27 04:27:00 | NPP-375D | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 0dac0054-ac88-3fb3-b779-782d68caa1f5 | -22.61035 | -49.03173 | 2025-09-27 04:27:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d340f54-d703-39d5-b791-5b297e54c8f1 | -22.59611 | -48.57351 | 2025-09-27 04:27:00 | NPP-375D | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 787ea203-8673-3809-b294-4200a80b0546 | -22.61247 | -49.03989 | 2025-09-27 04:27:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5c8156e-daa1-3288-b38a-c7d3504455c2 | -22.72128 | -51.39315 | 2025-09-27 04:27:00 | NPP-375D | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 27.5 |
| da4dd63b-c24c-3f8f-abac-9190be529b94 | -20.73343 | -57.77988 | 2025-09-27 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 36caae6d-fb00-3dc9-a4d3-014db8b73814 | -23.02989 | -46.70498 | 2025-09-27 04:27:00 | NPP-375D | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6a0b0c44-e0e9-3a20-8265-a11cc1dd806a | -23.06193 | -47.1954 | 2025-09-27 04:27:00 | NPP-375D | INDAIATUBA | SÃO PAULO | Brasil | 3520509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1e9739f1-f0b3-341a-9ec3-2d112903ff8a | -22.27037 | -46.42479 | 2025-09-27 04:27:00 | NPP-375D | OURO FINO | MINAS GERAIS | Brasil | 3146008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c8010635-ec81-3721-906f-c3bc64a09dcb | -22.61763 | -49.02921 | 2025-09-27 04:27:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8224c4f3-9494-3b5a-b60c-19c1170a217e | -21.68495 | -45.02253 | 2025-09-27 04:27:00 | NPP-375D | SÃO THOMÉ DAS LETRAS | MINAS GERAIS | Brasil | 3165206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4592fb4d-8645-3c98-bf3a-baf77f3de151 | -22.35799 | -49.464 | 2025-09-27 04:27:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 34ca4b99-4c57-33d6-89e6-f054ad1a1cde | -21.24848 | -48.57976 | 2025-09-27 04:27:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 148c695f-6c3c-330c-8ca7-e445e2aed989 | -22.5898 | -48.59164 | 2025-09-27 04:27:00 | NPP-375D | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 105e3c05-f573-3c62-bc24-ba89b332ce9e | -22.58254 | -48.59417 | 2025-09-27 04:27:00 | NPP-375D | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| d61cacf6-3e27-3ca4-85bb-b0bacc98fbb9 | -21.00521 | -50.00689 | 2025-09-27 04:27:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f6c2b77c-d64f-3b5c-a91a-8ce5190f4414 | -22.58921 | -48.59539 | 2025-09-27 04:27:00 | NPP-375D | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7566966c-4a4c-3753-90fa-5220b8f61789 | -23.8497 | -51.78627 | 2025-09-27 04:27:00 | NPP-375D | SÃO PEDRO DO IVAÍ | PARANÁ | Brasil | 4125803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 673e402d-6587-3229-abe1-36b2418bd8db | -22.85725 | -51.77814 | 2025-09-27 04:27:00 | NPP-375D | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| c1691b9f-c70f-340e-8967-e2eb11fbb0b7 | -22.72204 | -51.38887 | 2025-09-27 04:27:00 | NPP-375D | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 27.5 |
| cea57d7a-c648-36a1-9301-b987338a2b3d | -24.55409 | -50.68482 | 2025-09-27 04:27:00 | NPP-375D | TIBAGI | PARANÁ | Brasil | 4127502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4e404ab2-96f0-3ac6-b94a-9a8669a20b6a | -22.72557 | -51.38959 | 2025-09-27 04:27:00 | NPP-375D | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 02b4b35e-4852-39fa-8c09-f91d729c42b2 | -22.3796 | -49.4799 | 2025-09-27 04:27:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c863641f-bf3c-3483-9e41-54b3ea90713d | -22.27592 | -56.05331 | 2025-09-27 04:27:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d37d1d90-005e-3f57-8460-230785cf3831 | -21.00117 | -50.01461 | 2025-09-27 04:27:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e66e973e-71ae-397e-8f51-11f874c8900e | -22.21695 | -56.20074 | 2025-09-27 04:27:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb0522ad-084a-32ca-a39c-f537fbae83e0 | -21.00591 | -50.00736 | 2025-09-27 04:27:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8470c9ba-1fc2-375a-bfd0-c51a4603a379 | -20.12708 | -56.85313 | 2025-09-27 04:27:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5454caba-8840-3d7c-a078-980ebfcbb715 | -21.00525 | -50.01131 | 2025-09-27 04:27:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| eb2044a6-3694-3208-b42e-b375995cf712 | -22.52877 | -48.73845 | 2025-09-27 04:27:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d2c2d8da-5e90-31ea-b570-c267120422b1 | -22.38233 | -49.48436 | 2025-09-27 04:27:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b434bf73-b6e0-3e9e-9b84-177e63f46cde | -23.02929 | -46.70902 | 2025-09-27 04:27:00 | NPP-375D | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ec5790a2-8024-376d-8cfb-31b8b023c281 | -22.53095 | -49.11007 | 2025-09-27 04:27:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 53ac4e5f-b20f-398d-94bb-ccdce87a7737 | -22.58766 | -48.58353 | 2025-09-27 04:27:00 | NPP-375D | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 2f3b01a7-b076-38a6-a1ae-6523524b2e1d | -22.59002 | -49.0512 | 2025-09-27 04:27:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 256ecfd4-5b78-3876-a7c4-0c6dfa78b459 | -25.15081 | -50.14765 | 2025-09-27 04:27:00 | NPP-375D | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 08413e85-6d6d-3af4-aa82-374c8a3622f2 | -22.71699 | -51.39669 | 2025-09-27 04:27:00 | NPP-375D | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| 71e4e6b6-954d-3ace-8333-af88fe293fee | -22.72264 | -51.3906 | 2025-09-27 04:27:00 | NPP-375D | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 21.9 |
| 7f6cc5b3-50f6-3bc3-bd8f-979ab2be48af | -21.85616 | -57.11679 | 2025-09-27 04:27:00 | NPP-375D | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 15d2cfce-7c62-3946-8ded-278c3f6c3ad5 | -22.58825 | -48.57978 | 2025-09-27 04:27:00 | NPP-375D | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 9fa7fd6e-2274-3cce-a1c3-9c7236220b91 | -24.55342 | -50.68879 | 2025-09-27 04:27:00 | NPP-375D | TIBAGI | PARANÁ | Brasil | 4127502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 23932b26-27bd-368b-8fec-b280e3a3748c | -22.71836 | -51.39416 | 2025-09-27 04:27:00 | NPP-375D | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 21.9 |
| 342d13d3-8beb-301e-9f41-5ab84ad552ce | -21.48519 | -46.90918 | 2025-09-27 04:27:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7a5b4c28-bca0-3501-a7ba-5be8d5a38092 | -22.27477 | -56.05071 | 2025-09-27 04:27:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d94b1ece-8487-35a2-b020-cd9863c2b6a0 | -20.73794 | -57.78465 | 2025-09-27 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 373fe679-5373-3857-8929-9fd7923b8957 | -22.5904 | -48.58789 | 2025-09-27 04:27:00 | NPP-375D | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| e5d274b9-d7af-3a7c-a5f0-0bc4d96a677e | -20.99433 | -50.01327 | 2025-09-27 04:27:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| affcae7a-a5e0-376e-b867-c740f106a2c4 | -22.57409 | -48.60419 | 2025-09-27 04:27:00 | NPP-375D | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4ee1b6f9-2e0e-3d89-89b8-bab76c2f8592 | -24.47228 | -51.0214 | 2025-09-27 04:27:00 | NPP-375D | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 26abdddb-f9cf-3cd7-bdc5-4e8090b8aa55 | -22.36134 | -49.46463 | 2025-09-27 04:27:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b4485ef3-6f66-3779-8412-dd801449c5b7 | -22.85647 | -51.78262 | 2025-09-27 04:27:00 | NPP-375D | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 18.0 |
| 5e167f1f-16c0-3c8a-93aa-52959d56bd9b | -22.56567 | -48.61415 | 2025-09-27 04:27:00 | NPP-375D | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bbda72e6-6f24-3b27-84af-5d33b1fc5ee1 | -22.86004 | -51.78339 | 2025-09-27 04:27:00 | NPP-375D | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 31.1 |
| 9b9282d8-7a23-37ef-90c6-b3fef71c21d3 | -22.21338 | -56.19445 | 2025-09-27 04:27:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b09b8495-856d-3755-a8db-7c096afa9aae | -22.56293 | -48.60979 | 2025-09-27 04:27:00 | NPP-375D | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 490e129f-6736-30d6-87dc-d73077718093 | -22.38296 | -49.48055 | 2025-09-27 04:27:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52d4c536-bbde-394c-bb00-86203bfb308f | -20.99775 | -50.01393 | 2025-09-27 04:27:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |


[Clique aqui para ver as próximas entradas](README43.md)
