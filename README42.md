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
| 84b65e7b-3cca-3ed1-ab5c-4b245448c761 | -13.61504 | -48.0789 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| de349449-729b-3044-8118-d888b8a81421 | -15.03067 | -46.97432 | 2025-09-28 04:06:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c512a117-f86a-396e-b777-c659abd81eab | -12.89242 | -45.17166 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6276d4f4-c130-383d-895c-d03651eb9b09 | -11.44391 | -44.9993 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3217942c-5ef6-36b7-a0d8-3797a860d41c | -11.42448 | -44.9545 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bb36e6fc-fba0-36fb-9445-90b1899f27ed | -13.60572 | -47.29188 | 2025-09-28 04:06:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 616e02bc-c671-3e15-9c77-06d5abf9f6b4 | -10.41214 | -46.13997 | 2025-09-28 04:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14b9dc74-c9c4-31d9-9ad5-7765a7ae499e | -12.00577 | -47.0367 | 2025-09-28 04:06:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9cb62ecb-3c44-3fa3-b547-5c6cd4220c5f | -15.44441 | -48.22548 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7c2d02f0-ee8a-364a-8138-1d01abec89f1 | -12.94978 | -45.14959 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae7cb9a4-3318-3285-b67b-bf1dacd1900b | -14.77593 | -45.64979 | 2025-09-28 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38c897a8-c616-36ea-8f4e-5ebcc14bb416 | -12.91535 | -45.19441 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1844da4e-a2dc-3494-9b86-e9bfd96269b5 | -11.60298 | -45.43074 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f99c0172-c510-3b02-bc38-f9df95cd43d8 | -13.56257 | -44.10115 | 2025-09-28 04:06:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b2a9941-015c-3858-aef2-a31f49e8f2c8 | -11.85813 | -48.23559 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 313cce04-85f3-3f58-9211-546894d3e57f | -13.39993 | -48.15423 | 2025-09-28 04:06:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b453ccaa-bc7c-30a1-959e-de3c0dc4748a | -13.78613 | -47.88993 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 67e5cfc1-032e-3590-b2d9-6f648cae94e0 | -10.91706 | -44.80074 | 2025-09-28 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4c78510-ed73-3415-8495-2df8581fe266 | -10.04546 | -50.40404 | 2025-09-28 04:06:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a8585f7-b73c-3167-abc9-62dd833a1834 | -10.45311 | -50.8529 | 2025-09-28 04:06:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aae4019d-343a-3260-a6c2-3449d665388c | -13.80393 | -52.79183 | 2025-09-28 04:06:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6aaee491-3bef-31e2-b352-14faec984e31 | -15.28266 | -46.42427 | 2025-09-28 04:06:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b284348a-6a88-3ce6-90df-deff93412337 | -15.25344 | -43.08461 | 2025-09-28 04:06:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 18.4 |
| d9379a2c-bc11-3f7a-a48b-09c10ef98da8 | -13.00801 | -49.46074 | 2025-09-28 04:06:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8258ae42-a3c6-3129-afc7-ffe5dd739dd8 | -11.62576 | -52.86071 | 2025-09-28 04:06:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1904e183-357b-3d57-b15b-373a32741e8c | -13.43609 | -46.51783 | 2025-09-28 04:06:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2224f69d-271f-34d7-90d5-c0861aaf63b6 | -15.90042 | -46.21856 | 2025-09-28 04:06:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b0623a92-1e97-39ff-998c-425459457afa | -13.65127 | -42.38665 | 2025-09-28 04:06:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e93cc122-adf9-31f0-a7f7-6cfa11b4dcfa | -11.42253 | -44.9207 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2f70328a-e495-3148-ba72-82b091193b61 | -13.26191 | -48.45119 | 2025-09-28 04:06:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0015537-1396-3500-ac2f-56bdfd61089a | -15.33352 | -47.8958 | 2025-09-28 04:06:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3c045793-515f-3ff3-9919-8659d5b3769b | -11.43715 | -44.97082 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf23458d-d6b7-3129-8887-3c5681b5d4ad | -11.36422 | -44.94594 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1435442-c854-3480-bd0d-0a0e915fb9cb | -11.39676 | -46.93243 | 2025-09-28 04:06:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87e090c6-1316-3a82-88dc-1b319c77d62a | -12.98197 | -49.43837 | 2025-09-28 04:06:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 64436d56-f2b2-3fa4-aedd-00b08d8b0f93 | -15.81727 | -41.89008 | 2025-09-28 04:06:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 521578db-6957-3eef-885e-e7df31aa572d | -11.43413 | -46.64915 | 2025-09-28 04:06:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b97d657-5759-3711-aca7-63493c200e26 | -12.27813 | -44.04586 | 2025-09-28 04:06:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 58e179bd-333b-37f3-bc7e-3a26483ca399 | -11.36506 | -45.05221 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b911093c-32a0-35e0-a47e-2dff82d0e7d9 | -12.21281 | -43.74816 | 2025-09-28 04:06:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 015eff59-5704-3385-a231-7253649649fc | -11.77606 | -43.76696 | 2025-09-28 04:06:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab77e92c-f206-3e74-8aa5-45124674376c | -11.43069 | -44.91806 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4d6f13b3-8111-3dcd-85c0-7817a4f014b3 | -15.55444 | -47.89593 | 2025-09-28 04:06:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83481f19-b513-3944-841a-66096be7782a | -15.32431 | -47.89838 | 2025-09-28 04:06:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41c083eb-2470-3526-81e2-18e04dbb9d6e | -13.61699 | -47.3252 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 755b3949-6574-30e0-bca5-116369759917 | -13.39757 | -48.16731 | 2025-09-28 04:06:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fd70b7ec-b254-30ef-8a91-ebf42f67e279 | -14.53618 | -48.42217 | 2025-09-28 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 516942b7-7f0c-3520-8f60-2e72f7dd6c04 | -12.95065 | -46.3847 | 2025-09-28 04:06:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 15225f4d-fa9c-308d-9984-c6bc0297e512 | -12.28521 | -44.04714 | 2025-09-28 04:06:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b3ff56a-6489-3d3f-b7db-7ca1e48e0c40 | -13.2521 | -48.45347 | 2025-09-28 04:06:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d797ab21-bb90-39bb-9c7a-8bdeb8666641 | -12.00365 | -47.94761 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 67f66d3a-b2da-391c-8b8e-5db88c304316 | -11.43419 | -44.96549 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b3ee959-98ad-3b85-8133-643c5caddfcb | -13.58734 | -47.32177 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e552bb6-a4cd-3117-bb17-c803d13fa230 | -11.99846 | -47.89943 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94c92b64-5547-3955-a8f9-78a13c944550 | -11.35749 | -45.05104 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7a7c8c94-db67-3275-b965-bfbdf2f2340e | -13.31615 | -47.31366 | 2025-09-28 04:06:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4907ff70-fce1-347a-8b00-9947994d2184 | -14.83704 | -45.57088 | 2025-09-28 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 93d87468-8555-30d2-a942-c715c9b774af | -14.7725 | -45.69173 | 2025-09-28 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f3da0b6-900f-3cfc-8656-c965a9809940 | -13.62169 | -48.07339 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 612d02b6-0f6d-31d8-88d8-938b9424db8a | -11.58077 | -45.49138 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59e1a19b-9acd-3512-b423-a12fc7ad3c74 | -16.17736 | -43.64857 | 2025-09-28 04:06:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d695d94-666e-3bf0-b274-cf9cbd384a82 | -11.40606 | -44.90438 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a97fb421-dd2d-3708-a0e3-f66ff3118f2c | -11.37659 | -44.94102 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6222021-dd8c-345f-a635-d3828408b827 | -10.90615 | -45.76035 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 134685d1-729d-3f21-9bdb-3a5883aa19bc | -11.7964 | -44.90886 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 93e1b3c2-5292-325e-94fa-8f9652562dca | -13.59621 | -47.2967 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c3abf937-642f-3600-bf54-6e827b122f50 | -12.00655 | -47.95726 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ff1fbac6-6ad3-3614-a156-b484b0e41331 | -11.44843 | -44.99549 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3ecbda3b-5747-30d2-9a10-44676ca66f39 | -13.61651 | -48.07688 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5c87bb7d-f1fe-3ea0-a7c1-8abda18b6ae9 | -15.53391 | -47.9128 | 2025-09-28 04:06:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51a03431-85c4-346d-8749-7ef4e771dab1 | -12.88729 | -47.09661 | 2025-09-28 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 904c230b-b1fb-329f-9bcb-6aac08b6893b | -15.32856 | -47.89899 | 2025-09-28 04:06:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 94c262e2-ad84-31b4-8f9b-c62a719ac4c1 | -11.43791 | -44.96632 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 27d0979e-4603-37b9-aa6c-2c3f5926f35b | -14.58403 | -48.25846 | 2025-09-28 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| caac2f34-a582-30e4-8da1-58b45cfc5407 | -12.8269 | -44.68279 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac5992a2-dd73-3b09-996a-1e5d67ccb6a1 | -12.96093 | -47.21579 | 2025-09-28 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39808dd7-9f9a-348b-87b4-e5a5d874c6b7 | -13.31692 | -47.30931 | 2025-09-28 04:06:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19fdba77-54ee-390e-ad7a-a9618f038e5e | -11.69679 | -44.40567 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 14b5e8a6-6202-3b91-9c43-a2b86fb4a187 | -15.8206 | -41.89064 | 2025-09-28 04:06:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca608571-abd4-331c-8664-c039c9403bae | -10.7163 | -47.998 | 2025-09-28 04:06:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b5d7b33b-b4d4-349f-9750-46ed5e327a31 | -10.29381 | -45.39949 | 2025-09-28 04:06:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d6bcd477-34ce-392f-98da-bc21a0e36462 | -9.40625 | -54.69624 | 2025-09-28 04:06:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 58364154-3103-38bd-8021-d4001d501144 | -12.89908 | -45.17751 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| f40f2d4f-ff60-3d7c-80b3-6a707923f043 | -12.24102 | -46.7562 | 2025-09-28 04:06:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6278837f-8af7-3485-9146-b354d9edc2a8 | -11.41448 | -46.95583 | 2025-09-28 04:06:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4cfc1de-b731-3fc3-ac06-d796bec9b442 | -11.60413 | -45.43296 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6773f3ac-3825-33d8-a423-5a87c418c9ac | -14.77673 | -45.64518 | 2025-09-28 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9fcb0d29-4a06-3920-a969-f1103c96b884 | -11.3811 | -44.93727 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5914b264-8d94-30b0-a9e0-a43545c5a667 | -11.62222 | -52.85977 | 2025-09-28 04:06:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 19c13289-608a-36eb-b657-c9f58688095b | -11.98241 | -47.06935 | 2025-09-28 04:06:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8af56d3c-c605-3ba0-9689-0cfc1225d2e7 | -13.58625 | -47.30394 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a4fd2bea-8d93-3c2a-ab33-f84e394d748c | -11.95028 | -47.91018 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d8b1df3-76ee-34e4-bc6b-ecdfd08e21f9 | -13.58789 | -47.29496 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14cd8c2b-ba6e-3042-81c0-9c97aa19c00a | -15.26223 | -51.47962 | 2025-09-28 04:06:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eca5b0a2-a435-3a7e-8d24-b672571f6abb | -11.40528 | -44.90891 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b48c87f8-8b03-30e0-9332-aaa3d13a28a5 | -14.53966 | -48.42085 | 2025-09-28 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fee3808b-02d8-31cf-9f40-59ee7860e675 | -11.69316 | -44.40504 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1444e892-9e97-3578-b578-116e789f2219 | -12.00602 | -47.98611 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00ee65e9-9e32-30ce-b59e-cf5dddb9f2e3 | -11.98115 | -46.5924 | 2025-09-28 04:06:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21d46dec-f685-3d56-8e63-1496b31f194f | -11.51064 | -46.94827 | 2025-09-28 04:06:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README43.md)
