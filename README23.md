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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e2068c2-54d4-30e7-988b-36f950397e69 | -14.45524 | -45.62035 | 2026-08-21 03:45:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2b70c218-c34c-3469-a794-b37e541a3fd2 | -19.85119 | -43.87568 | 2026-08-21 03:45:00 | NPP-375D | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 5a748e80-274c-36d2-81f9-0d9471ce1127 | -15.16652 | -48.78038 | 2026-08-21 03:45:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 19534811-4a03-35ab-b623-693cf752cfc6 | -18.87647 | -42.03798 | 2026-08-21 03:45:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2797a33c-a5cd-37e9-9dd1-de0bbfb017a6 | -13.78178 | -43.18183 | 2026-08-21 03:45:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 854d1917-7638-3a11-ba35-5f530382456c | -19.67798 | -46.04395 | 2026-08-21 03:47:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 80714070-f5b6-37c7-9ea9-6147d5e0096c | -22.15955 | -46.65377 | 2026-08-21 03:47:00 | NPP-375D | SANTO ANTÔNIO DO JARDIM | SÃO PAULO | Brasil | 3548104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 66977406-7b51-3ee9-a933-c1b0bc747396 | -22.37876 | -43.01444 | 2026-08-21 03:47:00 | NPP-375D | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1de2c9d5-5518-3818-bd03-68c8bfbc3542 | -20.9685 | -44.61848 | 2026-08-21 03:47:00 | NPP-375D | SÃO TIAGO | MINAS GERAIS | Brasil | 3165008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2d47a03a-2c34-359d-9499-3bf8ebe821a9 | -20.96417 | -44.61386 | 2026-08-21 03:47:00 | NPP-375D | SÃO TIAGO | MINAS GERAIS | Brasil | 3165008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| aa081c09-f345-3c5a-8dd4-e3a8a1cb6f1f | -19.85925 | -45.52827 | 2026-08-21 03:47:00 | NPP-375D | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40bd222d-493b-3001-a66f-3e5a84379d4f | -19.91076 | -44.58774 | 2026-08-21 03:47:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5cd73961-4828-3836-86c0-a9c2fd60fbd8 | -21.49975 | -44.86176 | 2026-08-21 03:47:00 | NPP-375D | LUMINÁRIAS | MINAS GERAIS | Brasil | 3138708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 25e428ac-c6cc-35bd-aa4b-1723b7378f01 | -20.48371 | -43.40857 | 2026-08-21 03:47:00 | NPP-375D | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 01f2cb6c-cc6e-33f2-bff3-4b7959f6b5a4 | -23.53372 | -47.31479 | 2026-08-21 03:47:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 55bc65cd-2a49-37df-840c-f0d2d5eb6e66 | -21.88254 | -41.47449 | 2026-08-21 03:47:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e6c0caa1-a2a9-3b18-af31-d7190f53cea2 | -20.43332 | -46.49584 | 2026-08-21 03:47:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14885382-2aeb-31e6-9606-5d32ada87f9b | -21.57753 | -43.47807 | 2026-08-21 03:47:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 81722475-cf3a-3c88-b84b-2a4e9beb6c8e | -22.3816 | -43.02338 | 2026-08-21 03:47:00 | NPP-375D | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 43bcd3b0-6dc2-3a8b-9126-1e026a2c0d84 | -19.70077 | -46.91514 | 2026-08-21 03:47:00 | NPP-375D | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dcd03aa9-a59b-3803-9a8a-ecb61bd849f6 | -20.43878 | -46.49842 | 2026-08-21 03:47:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01519930-91e7-34ec-87dd-35e22ab3880a | -23.53271 | -47.319 | 2026-08-21 03:47:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 85bbb74e-d222-3a4b-a2a9-04a34a67f512 | -20.63721 | -41.2077 | 2026-08-21 03:47:00 | NPP-375D | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| db023b28-c6f2-3cc5-9416-91227c0c35bd | -22.18502 | -41.62133 | 2026-08-21 03:47:00 | NPP-375D | CARAPEBUS | RIO DE JANEIRO | Brasil | 3300936 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 673380b4-88e4-3efe-8c10-d971d924ced1 | -20.65704 | -46.19287 | 2026-08-21 03:47:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bafa1d43-035b-3e20-8b63-0a03fc6f58bc | -20.01853 | -45.53058 | 2026-08-21 03:47:00 | NPP-375D | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9fe21421-9943-3075-860d-ef251d90e5e4 | -19.67889 | -46.03981 | 2026-08-21 03:47:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7653b7c1-0ae4-3367-9d4d-7208d10dc826 | -23.53085 | -47.32044 | 2026-08-21 03:47:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4f848eab-efbe-305e-854c-a65db55e06b8 | -21.36608 | -44.13171 | 2026-08-21 03:47:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 694179ac-7d8e-3b86-90f1-cbac4729ef92 | -19.67145 | -46.04655 | 2026-08-21 03:47:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b91d1bdc-ac4e-3a57-b0d7-38d84d9c6096 | -19.86472 | -45.52955 | 2026-08-21 03:47:00 | NPP-375D | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6fc7f337-6e78-3cc6-b767-d388b320687e | -19.67055 | -46.05064 | 2026-08-21 03:47:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c93dd3a-8bfd-34c8-81ab-54996c3fe1e0 | -19.70684 | -46.91602 | 2026-08-21 03:47:00 | NPP-375D | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 209680c0-a76d-31a3-889f-d04a01b72fbe | -20.66247 | -46.19505 | 2026-08-21 03:47:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 256fff07-d57c-390e-8b58-07e52ed1d971 | -22.37706 | -43.02283 | 2026-08-21 03:47:00 | NPP-375D | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1026006f-b178-3644-bd99-4d04fed96cf2 | -20.43416 | -46.49213 | 2026-08-21 03:47:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5926e100-5c69-314d-a23d-0131ec790a56 | -22.16212 | -46.65539 | 2026-08-21 03:47:00 | NPP-375D | SANTO ANTÔNIO DO JARDIM | SÃO PAULO | Brasil | 3548104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| bcd7693e-6d6d-359d-927b-0cad8c067827 | -19.91048 | -44.58791 | 2026-08-21 03:47:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f3f4dc52-ee9f-31b5-934a-7b6830996081 | -21.01057 | -44.85484 | 2026-08-21 03:47:00 | NPP-375D | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5edac20f-9450-3590-9e31-fd9cf83189ac | -20.43972 | -46.49425 | 2026-08-21 03:47:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fbc70713-09bf-3556-8f58-bc4fe02114c2 | -21.57643 | -43.48335 | 2026-08-21 03:47:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 5196f8ef-9474-3bf2-a9f0-2aa69a958843 | -21.32586 | -43.80634 | 2026-08-21 03:47:00 | NPP-375D | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| e98226f9-618f-36e6-bc35-ded531b62199 | -19.66579 | -46.04524 | 2026-08-21 03:47:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 61fa18b7-79bc-3fdc-ba6d-fc59e9f403e0 | -21.4991 | -44.86475 | 2026-08-21 03:47:00 | NPP-375D | LUMINÁRIAS | MINAS GERAIS | Brasil | 3138708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2fa7728b-422d-38f6-830a-999e3f32141b | -20.41908 | -41.58976 | 2026-08-21 03:47:00 | NPP-375D | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f702ab02-37c4-37cb-ac8e-893e1d8fc962 | -20.258 | -46.73895 | 2026-08-21 03:47:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52ba98c2-28ff-36f3-8d2b-aa6dc9f19d4d | -21.0157 | -44.85605 | 2026-08-21 03:47:00 | NPP-375D | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ea3b5e44-8738-3f37-a5f2-0988eb6d4d2c | -20.78348 | -45.10003 | 2026-08-21 03:47:00 | NPP-375D | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| eac0607f-3947-34e3-b1bb-e048337367a5 | -21.36727 | -44.12606 | 2026-08-21 03:47:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 32fbb605-abd6-32f4-bfe0-d9acb96600aa | -20.65953 | -46.19139 | 2026-08-21 03:47:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6a4a2267-65f8-3d35-b0ce-9f16914e1da7 | -21.32473 | -43.81178 | 2026-08-21 03:47:00 | NPP-375D | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| fd116bb8-4953-33bf-90cc-c5568ef89f83 | -20.9692 | -44.61515 | 2026-08-21 03:47:00 | NPP-375D | SÃO TIAGO | MINAS GERAIS | Brasil | 3165008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1355ff79-0d99-311c-97c2-15092e1fc3b7 | -20.83495 | -44.19508 | 2026-08-21 03:47:00 | NPP-375D | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| f3ca3af9-273f-39d1-a887-8b5fab4747be | -23.53185 | -47.31609 | 2026-08-21 03:47:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 32138c31-eb65-3d7a-9cbd-f84f73e0d2e0 | -22.66149 | -42.80555 | 2026-08-21 03:47:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f63f02ae-84e8-32da-a70a-7391632a49b6 | -21.88663 | -41.4754 | 2026-08-21 03:47:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e1e510b9-3362-30cd-a9e9-7983afe0acc8 | -20.65851 | -46.19587 | 2026-08-21 03:47:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6801923c-1ce4-3ad1-b3bb-a9c9141e743d | -22.51734 | -42.64004 | 2026-08-21 03:47:00 | NPP-375D | CACHOEIRAS DE MACACU | RIO DE JANEIRO | Brasil | 3300803 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7668ade2-4a90-3e18-8d19-a2ed38888d81 | -20.48408 | -43.40606 | 2026-08-21 03:47:00 | NPP-375D | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 6a3b0cc9-7fd7-30df-be66-5c78c6e98a11 | -19.67234 | -46.04254 | 2026-08-21 03:47:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c87a352a-0d4d-34c9-96c6-c84f033456f9 | -20.25908 | -46.73415 | 2026-08-21 03:47:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 143ce766-f423-3e69-a86c-a7a51ba2be6e | -23.53752 | -47.31742 | 2026-08-21 03:47:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 634583ee-91af-3ee0-ac0c-1a5ec0f733f7 | -20.83001 | -44.19398 | 2026-08-21 03:47:00 | NPP-375D | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3203e549-d882-303f-bf97-1d19a2d08c17 | -19.66489 | -46.04928 | 2026-08-21 03:47:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d556040e-5a4b-30b3-94bf-a8e6672bb6e0 | -20.65606 | -46.19734 | 2026-08-21 03:47:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9e968a4-6738-3a31-9ed7-f012f5a6ddbf | -20.31941 | -42.74036 | 2026-08-21 03:47:00 | NPP-375D | URUCÂNIA | MINAS GERAIS | Brasil | 3170503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| be6e6f95-69e3-393e-b0ec-57ba371b66a0 | -22.15868 | -46.65767 | 2026-08-21 03:47:00 | NPP-375D | SANTO ANTÔNIO DO JARDIM | SÃO PAULO | Brasil | 3548104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 82177ce4-fee3-3a01-817c-d0befc715f36 | -22.3779 | -43.01865 | 2026-08-21 03:47:00 | NPP-375D | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d2e474a6-36d3-3b43-8c17-21cd22ee4599 | -19.664 | -46.05332 | 2026-08-21 03:47:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e07edae4-4d09-3cf2-a46b-5eb4ec7650b1 | -12.4914 | -54.7569 | 2026-08-21 03:50:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 1ec4f980-bed8-34f6-bfa9-88d4652d923f | -11.1747 | -54.0216 | 2026-08-21 03:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 59233eab-6ce9-3eb4-ae1a-6cffdc217c8e | -9.4257 | -60.416 | 2026-08-21 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 133.9 |
| 0aa38cf7-72f1-303d-9553-5912640e63c2 | -9.4071 | -60.417 | 2026-08-21 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 237.9 |
| af05cf10-0e16-346a-a5f2-d0276c8be9e1 | -9.4072 | -60.3977 | 2026-08-21 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 8f96f15f-1920-3e26-bef1-888d525128fb | -12.5104 | -54.755 | 2026-08-21 03:50:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 21334799-e8fb-3ae7-89d1-ec4b30a0198b | -6.8939 | -59.4356 | 2026-08-21 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 2638a823-4b38-376b-a49f-91b33df8fded | -11.1558 | -54.0233 | 2026-08-21 03:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 7c42d665-29c4-36d3-9459-57b46ddf9908 | -7.3605 | -45.791 | 2026-08-21 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 466aa573-4012-3d15-a1a3-8a7a91ad1740 | -6.8756 | -59.4171 | 2026-08-21 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 401bfa02-5d1b-3e33-a2ae-00b17d3eb331 | -9.4259 | -60.3967 | 2026-08-21 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| c844eb0e-eed0-3e42-9f7e-cac4b06b134a | -6.2156 | -55.6118 | 2026-08-21 03:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 048f964e-7fd1-3d8f-81d2-e334143e73a3 | -8.3903 | -62.6963 | 2026-08-21 03:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 1072f65d-4310-36f8-8e84-a15d243deb56 | -11.175 | -54.001 | 2026-08-21 03:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 2e6d588a-fffe-3932-bdb7-e94fbe80197e | -7.3603 | -45.8136 | 2026-08-21 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 267.9 |
| 7f8b4e9c-c072-3f72-b0c7-66f2f444f63e | -9.4069 | -60.4362 | 2026-08-21 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 87f4f768-dd0d-3392-87a7-f827037df375 | -6.8755 | -59.4364 | 2026-08-21 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 82932348-238b-34fe-b41f-662cb8364821 | -7.3415 | -45.8152 | 2026-08-21 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 3e3ac911-04fb-3b3f-9474-55d913eca947 | -3.5406 | -48.1889 | 2026-08-21 03:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 1015878a-463a-3d6b-a051-273704fe5ba2 | -6.2341 | -55.6109 | 2026-08-21 03:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 218efb61-18fc-3dbb-89a9-7549c3dc1339 | -9.3885 | -60.4179 | 2026-08-21 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| ea02f43d-66d6-3758-b7ed-ebf031f57172 | -6.2155 | -55.6316 | 2026-08-21 03:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 25ebca4b-a196-3797-a8db-e58dc856b0c9 | -6.6938 | -58.942 | 2026-08-21 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| c9289501-dc8c-3900-bb7e-2c3d28058cc5 | -7.3791 | -45.8119 | 2026-08-21 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 09ebbeb3-0152-30d1-87fa-7adedddec9e4 | -9.4257 | -60.416 | 2026-08-21 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 7c7f46a8-00df-3f4a-ab9b-6a183a89483b | -7.3791 | -45.8119 | 2026-08-21 04:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 104.6 |
| d9eca666-87bd-3499-a248-f702c6fd422c | -6.1361 | -59.9063 | 2026-08-21 04:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 1d236194-d28f-3e77-9756-f13f4c131048 | -7.3605 | -45.791 | 2026-08-21 04:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 7e3ff77e-525c-3004-aabd-63d6813cc464 | -11.175 | -54.001 | 2026-08-21 04:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 1966353b-d68e-3c38-852d-9a32ffe72b24 | -8.3718 | -62.697 | 2026-08-21 04:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.0 |
| d0b1d336-ee7b-3b02-919c-e28555f5ef66 | -7.3603 | -45.8136 | 2026-08-21 04:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 200.4 |


[Clique aqui para ver as próximas entradas](README24.md)
