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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d1f532d-6133-34a1-905e-7d3bd1abfe1a | -12.32534 | -53.27421 | 2026-07-22 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa9caf6f-bfbd-3d72-a2cf-f2b9017e0992 | -15.43922 | -55.89194 | 2026-07-22 04:46:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c212a0f4-fd45-38cc-b675-30430de6a95b | -15.4389 | -55.89456 | 2026-07-22 04:46:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c62f567c-2862-3e4e-a1fe-b22a5b95ae9a | -17.58468 | -47.51378 | 2026-07-22 04:46:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0821331d-889f-310c-9ece-f54ab4113ae0 | -17.67732 | -47.22446 | 2026-07-22 04:46:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80397475-606f-3c50-a50e-469f33b966b2 | -12.51733 | -48.25682 | 2026-07-22 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 194fbe0c-a145-3d7d-bb68-6a319b383881 | -17.57927 | -47.49984 | 2026-07-22 04:46:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 15.6 |
| cc182df6-1f7b-3387-a5ae-96aa88a4d153 | -13.44265 | -43.6744 | 2026-07-22 04:46:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c3d864e-a8d8-30f6-878b-f966c842e5d4 | -12.45771 | -46.51256 | 2026-07-22 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d72e956e-7d6d-324a-aea6-7ce7c46d0681 | -17.57068 | -47.50043 | 2026-07-22 04:46:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 713e7801-6c6e-3062-8d18-9b1f7a2572bc | -12.32638 | -50.00716 | 2026-07-22 04:46:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7210fa1c-d664-398a-b049-c269100b671d | -12.13985 | -48.25714 | 2026-07-22 04:46:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a46944d6-e694-3d72-909d-f6d725ee1ef4 | -14.25765 | -54.76296 | 2026-07-22 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1ac976ac-3fb1-3ac3-bc70-8b5a41b306d8 | -17.84228 | -52.48621 | 2026-07-22 04:46:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cb5a848b-890f-3aab-84da-5a10ea2776f3 | -19.19767 | -46.44762 | 2026-07-22 04:46:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c790221d-a6c6-345c-b55d-c389d9303565 | -17.58288 | -47.50038 | 2026-07-22 04:46:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 42dc7f79-a32b-370c-97c9-b78431c1b2f4 | -17.73441 | -52.74915 | 2026-07-22 04:46:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d586f695-278a-3385-bc14-5151cdd0ecd1 | -12.32431 | -53.27622 | 2026-07-22 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd6243e8-00d9-3941-bc57-a9bb50a56f12 | -17.7257 | -48.60005 | 2026-07-22 04:46:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f362055e-92ea-3a10-b48f-978e0b850f37 | -17.57086 | -47.50733 | 2026-07-22 04:46:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b136a20a-761e-3d45-a381-9ae9983714c6 | -15.24048 | -48.25332 | 2026-07-22 04:46:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06dbae3d-f788-301a-8833-e96b3c5680fd | -17.73785 | -52.74979 | 2026-07-22 04:46:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 614b6d77-6b84-3194-ae12-b6d560524cac | -18.27156 | -43.69768 | 2026-07-22 04:46:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 048910ff-8837-3a4e-b69e-08df01eb1163 | -17.58528 | -47.50953 | 2026-07-22 04:46:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e5b12068-07d5-3144-a041-8126ef37f1a7 | -13.99038 | -49.59361 | 2026-07-22 04:46:00 | NPP-375D | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5e0b78ea-68de-34ba-9668-cb80f5a84764 | -17.57506 | -47.50361 | 2026-07-22 04:46:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 8a9b3172-4039-3bbe-86e5-0b6f69b4f156 | -12.32453 | -53.27878 | 2026-07-22 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0c2a823-fc51-3b06-8d3b-01daac243dd2 | -15.43964 | -55.89061 | 2026-07-22 04:46:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0af0dbc6-2760-3d91-af39-d7f7eceb4f9d | -17.58227 | -47.50471 | 2026-07-22 04:46:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ce450cb8-79f4-3e46-b5ec-e73b40ec2808 | -17.58048 | -47.51749 | 2026-07-22 04:46:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c106df6b-35a5-33d2-bd33-1c6e33dd0137 | -12.52406 | -48.25788 | 2026-07-22 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bd55631d-5e8a-3521-b319-64fccb370dae | -13.84977 | -53.90028 | 2026-07-22 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e29e1f1-392b-37a9-92ce-b4eff9e6a63e | -12.37444 | -45.67532 | 2026-07-22 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b821e54f-1274-38a9-84d8-5a7c18aa0e5f | -16.48557 | -49.00923 | 2026-07-22 04:46:00 | NPP-375D | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd1b1ec6-a70f-353e-8ac5-20734f1ee9d0 | -12.00177 | -49.26937 | 2026-07-22 04:46:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b9fabdc-e3e0-3352-b9f0-a5818a052db8 | -13.44208 | -43.67857 | 2026-07-22 04:46:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca4f3ec9-df98-3418-8a43-4967fa976a8f | -17.57746 | -47.51274 | 2026-07-22 04:46:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 8f504b6b-c851-334f-80ef-e7abd447fa54 | -23.4265 | -46.75932 | 2026-07-22 04:49:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fd8705fc-94b1-3f41-8d2d-03b80ef5def8 | -23.2772 | -46.16195 | 2026-07-22 04:49:00 | NPP-375D | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 43f971a5-83d2-30c1-a692-7aa704f9ec31 | -21.70222 | -47.16814 | 2026-07-22 04:49:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e948140c-6dc8-38d7-8479-b709a6f0a3ad | -22.43932 | -42.63187 | 2026-07-22 04:49:00 | NPP-375D | CACHOEIRAS DE MACACU | RIO DE JANEIRO | Brasil | 3300803 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| ed9ef670-44ed-3f69-87db-0a705884a12a | -23.94892 | -47.22058 | 2026-07-22 04:49:00 | NPP-375D | IBIÚNA | SÃO PAULO | Brasil | 3519709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| eb293997-aa81-3d35-a9e2-678eff4a03c6 | -22.24449 | -48.38395 | 2026-07-22 04:49:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 681f0168-bd64-378f-ad47-8dbf0905095b | -22.44358 | -42.63163 | 2026-07-22 04:49:00 | NPP-375D | CACHOEIRAS DE MACACU | RIO DE JANEIRO | Brasil | 3300803 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 54ebc2ed-7c47-3e71-b079-896c9bfff5b4 | -23.51953 | -47.21432 | 2026-07-22 04:49:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| c09879e9-8e8c-3716-b1aa-a2e84165a622 | -23.94694 | -47.2214 | 2026-07-22 04:49:00 | NPP-375D | IBIÚNA | SÃO PAULO | Brasil | 3519709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4fa68c9f-b7cf-3dba-95e7-09abcbdda68a | -23.27183 | -46.68002 | 2026-07-22 04:49:00 | NPP-375D | FRANCISCO MORATO | SÃO PAULO | Brasil | 3516309 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 841d09fc-8b6f-31ae-bdc0-c7528e4d2b83 | -21.97092 | -41.11293 | 2026-07-22 04:49:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2a3f4f9a-3f35-37f2-9a70-3fb32ca37708 | -21.70412 | -47.16488 | 2026-07-22 04:49:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9e933f8f-3655-3a1e-b899-a3dcdc02acfd | -21.19938 | -47.8844 | 2026-07-22 04:49:00 | NPP-375D | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4e6dfc37-928c-3cd9-8b0c-5f394281d4ed | -21.70607 | -47.16875 | 2026-07-22 04:49:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2959819b-391f-302c-b5d0-1529e3073737 | -23.94762 | -47.21585 | 2026-07-22 04:49:00 | NPP-375D | IBIÚNA | SÃO PAULO | Brasil | 3519709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 000916ca-eb40-397f-a2b5-c49e1fd6fb07 | -22.79619 | -49.34137 | 2026-07-22 04:49:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5a87544c-a5ba-3ffb-91e2-cc11b9cc4d67 | -22.2094 | -49.73161 | 2026-07-22 04:49:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9e1778e7-faaf-3f8b-a103-2ec91e91b2f6 | -23.192 | -46.29778 | 2026-07-22 04:49:00 | NPP-375D | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 184ef558-876a-3cf2-bc5f-e1871642295c | -23.52094 | -47.21352 | 2026-07-22 04:49:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| b8bc9081-f42c-3e37-97ec-a1d83995583f | -22.44329 | -42.63445 | 2026-07-22 04:49:00 | NPP-375D | CACHOEIRAS DE MACACU | RIO DE JANEIRO | Brasil | 3300803 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 6a8869f3-5a6e-3329-8c89-118910ee3af2 | -19.51092 | -49.68293 | 2026-07-22 04:49:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a8c3ea98-5762-33c6-9277-662a9ae72940 | -21.14648 | -50.46567 | 2026-07-22 04:49:00 | NPP-375D | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b55f47c7-7f9a-3343-89ef-e14dd90c94a2 | -23.9509 | -47.22201 | 2026-07-22 04:49:00 | NPP-375D | IBIÚNA | SÃO PAULO | Brasil | 3519709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0b3facfc-7222-3d51-b2cb-76d0ef496d9f | -23.17974 | -46.1209 | 2026-07-22 04:49:00 | NPP-375D | IGARATÁ | SÃO PAULO | Brasil | 3520202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| ce1f84fe-248e-347f-b0da-1916d3ab0641 | -21.2 | -47.8798 | 2026-07-22 04:49:00 | NPP-375D | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 63a47cea-6f44-3a8a-bd12-9a0ce7477a73 | -18.53942 | -56.81917 | 2026-07-22 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e2d977f0-e2bb-3c03-949a-ecd212473e26 | -23.28137 | -46.16265 | 2026-07-22 04:49:00 | NPP-375D | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 603568de-f85f-317f-81ab-34c23bf4069e | -22.4381 | -42.63378 | 2026-07-22 04:49:00 | NPP-375D | CACHOEIRAS DE MACACU | RIO DE JANEIRO | Brasil | 3300803 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| efa7b776-7439-3ea8-8a3f-e8dcf321ca3f | -19.99527 | -44.25381 | 2026-07-22 04:49:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| cfe9ea23-c0f3-39e3-baa7-3694d330c30a | -20.70719 | -47.29063 | 2026-07-22 04:49:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 05a848d3-e4d6-35b1-b45a-428d04209ac3 | -23.18023 | -46.1168 | 2026-07-22 04:49:00 | NPP-375D | IGARATÁ | SÃO PAULO | Brasil | 3520202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 9419bfd2-58cd-3aa0-be82-56bd514f16c5 | -18.53865 | -56.8232 | 2026-07-22 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 9e7d7681-7af7-3982-9221-9369b568ce77 | -23.13889 | -48.67731 | 2026-07-22 04:49:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 43c4b2d8-2384-3a6e-8597-8e190a28ac47 | -22.14253 | -44.51654 | 2026-07-22 04:49:00 | NPP-375D | BOCAINA DE MINAS | MINAS GERAIS | Brasil | 3107208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 888d3c99-7c15-3584-b09d-b4e3087591d4 | -18.9327 | -52.59712 | 2026-07-22 04:49:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 755e3553-533f-34b1-b152-a9208d3cf080 | -23.14313 | -48.67327 | 2026-07-22 04:49:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb06cd00-e9cc-396c-9e19-3760c709d7d4 | -21.29004 | -41.74284 | 2026-07-22 04:49:00 | NPP-375D | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dd5efd64-9b45-3cc1-b362-dd009049e090 | -18.54439 | -56.816 | 2026-07-22 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 4f56bfb7-9e41-3b3a-b945-19167d2a4fbb | -23.184 | -49.69309 | 2026-07-22 04:49:00 | NPP-375D | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c5e6d995-9e6d-3db8-bf01-bb0a1908ef8c | -21.13184 | -47.97447 | 2026-07-22 04:49:00 | NPP-375D | SERTÃOZINHO | SÃO PAULO | Brasil | 3551702 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0d7c10a1-0265-38f7-b5e1-4b62875080ea | -23.76864 | -47.44566 | 2026-07-22 04:49:00 | NPP-375D | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f779f2b2-b6a1-3b55-8c45-82fac6b15c07 | -22.4445 | -42.63266 | 2026-07-22 04:49:00 | NPP-375D | CACHOEIRAS DE MACACU | RIO DE JANEIRO | Brasil | 3300803 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| bea656a1-4c93-3998-8424-7337d6e8a30e | -23.19618 | -49.15248 | 2026-07-22 04:49:00 | NPP-375D | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0d451d1-5ad3-38ae-a0f6-6f2ad5bcc8ab | -22.207 | -49.73243 | 2026-07-22 04:49:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fb65fd95-2735-37a2-bc39-a41b9a2f6bf9 | -18.53679 | -56.81023 | 2026-07-22 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 66681cf8-8be7-35fd-a73f-8b2d255c3d37 | -18.53524 | -56.8183 | 2026-07-22 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| fd524cc4-ed97-3805-bb59-98a323ea873e | -19.71681 | -50.20978 | 2026-07-22 04:49:00 | NPP-375D | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 5452058e-aa90-3cb1-be58-a34817a4dde8 | -23.28186 | -46.15858 | 2026-07-22 04:49:00 | NPP-375D | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| afe53458-12bf-37b6-b360-291ed82d0181 | -23.18053 | -49.69246 | 2026-07-22 04:49:00 | NPP-375D | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f69d2dbe-dd1b-31e8-9a45-c4f678701f29 | -21.28553 | -48.54657 | 2026-07-22 04:49:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47d0beff-b2d4-3170-9bcf-a3f2523a93d5 | -18.54362 | -56.82004 | 2026-07-22 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 83cf2d68-fadc-3a33-8cbc-59919ac7a4d1 | -18.53339 | -56.80533 | 2026-07-22 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 38ecdec8-996b-33b1-bff0-2c25482d2919 | -18.5402 | -56.81514 | 2026-07-22 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e860af80-4841-3c3a-b50e-fb328df5f254 | -21.59869 | -46.06351 | 2026-07-22 04:49:00 | NPP-375D | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0103f82d-52d6-38af-ac31-b8fdc1361206 | -20.3609 | -46.61285 | 2026-07-22 04:49:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4904b75f-84fe-3478-878a-0c5ef4169998 | -23.51703 | -47.21281 | 2026-07-22 04:49:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e324a9ba-6d9e-32ae-b645-3757f71fe93a | -20.71096 | -47.29121 | 2026-07-22 04:49:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2b4a4b67-96ea-3edd-903d-558fbc2d9e29 | -22.43841 | -42.63084 | 2026-07-22 04:49:00 | NPP-375D | CACHOEIRAS DE MACACU | RIO DE JANEIRO | Brasil | 3300803 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c9ce9cf4-429c-3978-84fd-8fc1b0244cc2 | -18.53261 | -56.80935 | 2026-07-22 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| bcaf271e-6d25-36f2-b43b-e6fbf9c9e793 | -23.17553 | -46.12046 | 2026-07-22 04:49:00 | NPP-375D | IGARATÁ | SÃO PAULO | Brasil | 3520202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 5a0dd0d6-6436-3042-b13d-a04b56a6ae73 | -22.14324 | -44.51522 | 2026-07-22 04:49:00 | NPP-375D | BOCAINA DE MINAS | MINAS GERAIS | Brasil | 3107208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b633b14a-93c0-39e9-a2e0-bd0f88de305c | -21.88762 | -45.56416 | 2026-07-22 04:49:00 | NPP-375D | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8e9c2d7e-001c-318d-86ea-c4d99f84e228 | -23.17603 | -46.11632 | 2026-07-22 04:49:00 | NPP-375D | IGARATÁ | SÃO PAULO | Brasil | 3520202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |


[Clique aqui para ver as próximas entradas](README9.md)
