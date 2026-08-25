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
| b9d941e8-35ed-333d-a7b0-1a3449e9c15b | -8.76419 | -45.79314 | 2026-08-25 04:08:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8b7d2fe-f25b-38eb-84f6-c262b0dac3ca | -11.98815 | -45.92614 | 2026-08-25 04:08:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c86df8c-336b-3b98-94c0-aec6e2779c07 | -12.71169 | -48.39395 | 2026-08-25 04:08:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 45719eb0-68db-3db8-a7bf-f857a55798a3 | -7.90132 | -46.36158 | 2026-08-25 04:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| a89a9001-fe63-3d87-b8ba-369e4cd976f5 | -12.74764 | -46.46125 | 2026-08-25 04:08:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ed1e8b2-4ac8-3875-8599-029ce1e80cc8 | -7.74114 | -46.1563 | 2026-08-25 04:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 657531af-d77f-30ea-8c29-90dd2dbd569f | -8.10079 | -47.47139 | 2026-08-25 04:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71ada838-17c8-3ce3-acd5-d8c7f6ef6dae | -11.98386 | -45.91806 | 2026-08-25 04:08:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38288735-35c3-33bb-a317-9bda49d4dd65 | -10.78285 | -50.93109 | 2026-08-25 04:08:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5a1b2c23-7eee-3624-8898-9c95aebee660 | -10.79599 | -50.92891 | 2026-08-25 04:08:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 376c4032-74cf-32c6-b71d-276f7e9b3996 | -8.0956 | -47.4708 | 2026-08-25 04:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b55b436f-b940-3b66-a746-a55ac033a532 | -12.75279 | -46.45804 | 2026-08-25 04:08:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33bec557-f78c-3e55-8e89-e08a3c18c0bb | -8.07306 | -44.6544 | 2026-08-25 04:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 44bdabf5-398f-30c2-8750-5012a069df6e | -10.48212 | -50.44386 | 2026-08-25 04:08:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08624197-57d0-3bad-ac09-aa537d202134 | -8.06948 | -44.64977 | 2026-08-25 04:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 36453171-f699-3103-9101-83d99b4bce98 | -6.84273 | -52.49971 | 2026-08-25 04:08:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3d1b3a5a-371d-3ad4-a7fc-91ecfd2ed793 | -12.60977 | -44.63153 | 2026-08-25 04:08:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40d825c7-3ad0-3648-aa8e-07c073f8eca7 | -12.14174 | -50.61058 | 2026-08-25 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8906ffeb-8c3c-36ad-89fd-bae4268c664d | -12.20794 | -43.17144 | 2026-08-25 04:08:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e03b3a62-6e8e-3818-91ae-473b586af926 | -8.9376 | -50.16353 | 2026-08-25 04:08:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 38221f71-5aac-3de3-9d61-24cd61147195 | -12.13244 | -45.12156 | 2026-08-25 04:08:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fc5e5fa5-2a1b-31f8-984a-e505a4613e2f | -9.46272 | -40.32769 | 2026-08-25 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| d7bea748-9cb1-3ec8-86c2-06e1997b85b4 | -12.70562 | -48.39849 | 2026-08-25 04:08:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9b231595-c87b-3db2-9c02-b00704af294d | -12.7759 | -44.25705 | 2026-08-25 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a64cfa18-fd68-345f-8a58-170564ad6dc7 | -9.69488 | -46.05598 | 2026-08-25 04:08:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ebc2c130-aef2-3f9c-b572-8784f237dd01 | -11.43704 | -44.54785 | 2026-08-25 04:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 239aa0ae-ce30-38e5-8948-e2ca55392ec3 | -12.7596 | -46.44558 | 2026-08-25 04:08:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25475318-da11-300e-9f9a-71050dcaded4 | -9.9756 | -48.3188 | 2026-08-25 04:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 354639b0-e02d-365d-bc48-7f444106188e | -9.93238 | -40.49664 | 2026-08-25 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 19e45e8a-174b-3a0c-ba31-e9e029d1f2f9 | -7.74094 | -46.1548 | 2026-08-25 04:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3489ceac-b75f-39f2-a43a-13505c1b05b5 | -7.90015 | -46.36353 | 2026-08-25 04:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c7e58260-5045-3441-9abc-4979987980dc | -11.16591 | -54.00335 | 2026-08-25 04:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d7da2e5e-1e52-3a0a-8168-dd741959cb2e | -12.84481 | -48.49925 | 2026-08-25 04:08:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 45736255-90f6-32b3-870f-6434c59e72ce | -8.16552 | -46.69999 | 2026-08-25 04:08:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78372dcc-0e7d-3194-902e-5abea9dbb07d | -9.3344 | -40.30338 | 2026-08-25 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 316de587-9cbd-3d9c-a713-094cf7fddf7c | -8.11055 | -47.47613 | 2026-08-25 04:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff150131-cdd5-3e70-9e08-32f223680290 | -7.89539 | -46.38979 | 2026-08-25 04:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 34647d09-e41a-39c2-9705-ecfdfcaa2061 | -15.69087 | -43.28635 | 2026-08-25 04:08:00 | NPP-375D | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 14932a98-38ba-30ae-8758-f50b4c21d800 | -8.08783 | -47.51403 | 2026-08-25 04:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dff7a2b5-2c2b-341a-9831-f8b097e7ab39 | -10.77675 | -50.92982 | 2026-08-25 04:08:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ece8d7ad-4d67-3e74-9d0a-233f99be219f | -10.30472 | -48.20362 | 2026-08-25 04:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1033e46b-972a-3c09-90a5-ff300819f9d0 | -8.06881 | -44.65369 | 2026-08-25 04:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8c463831-29c7-346c-ac57-2283d8ef046a | -8.07015 | -44.64585 | 2026-08-25 04:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f9e76780-dd05-3081-aaa9-651e5af85cc9 | -6.9461 | -52.79401 | 2026-08-25 04:08:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7efc8363-5a05-3172-a02e-0229683bd876 | -13.35587 | -48.19702 | 2026-08-25 04:08:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9821c377-214f-32d5-b694-7bea628ffd77 | -12.72109 | -48.38981 | 2026-08-25 04:08:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85378823-c85d-30fd-be6d-d02d66ba6b64 | -12.70612 | -48.39584 | 2026-08-25 04:08:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7459e268-268d-392e-8371-908743d2cbfe | -7.90295 | -46.37533 | 2026-08-25 04:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f2fe0574-92c9-30b8-982a-215615c9dc5e | -9.96921 | -48.32385 | 2026-08-25 04:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 18b696dc-c46a-3962-a84c-9703feac07cc | -15.53484 | -40.85596 | 2026-08-25 04:08:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3651f4cd-7709-384c-9a84-a49f5c69cc17 | -10.0412 | -46.40796 | 2026-08-25 04:08:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 32e4e61f-2d45-370c-aa3d-004377df1b39 | -13.35322 | -48.21083 | 2026-08-25 04:08:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 9846a2b3-9aee-3fe2-82a4-f889421a7c65 | -9.60082 | -45.38085 | 2026-08-25 04:08:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4d193ec3-ae3c-38ef-8b55-9161c3518a0b | -8.07931 | -47.53177 | 2026-08-25 04:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a99a2ab7-418b-349e-a495-fe9929630af1 | -12.12914 | -43.38774 | 2026-08-25 04:08:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ca4d227-0863-3d4a-8e80-3400d027525c | -10.37196 | -45.06678 | 2026-08-25 04:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f2d9ad55-bd19-3e62-a4f3-36d317e1721b | -10.77581 | -50.93455 | 2026-08-25 04:08:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1ae2746c-bdb0-3f8f-96d9-af240c181cf0 | -11.88609 | -43.83014 | 2026-08-25 04:08:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 48a20580-d76b-3462-acc4-6fa1022928c3 | -11.97671 | -45.90807 | 2026-08-25 04:08:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ce236d9-1178-3f42-a154-e1db7abd9f18 | -7.76182 | -46.14965 | 2026-08-25 04:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0de1e523-8453-3973-85e7-8a40089f48e9 | -11.44104 | -44.54858 | 2026-08-25 04:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0ffeb21f-9604-3a3b-9df0-c75eb243ffea | -11.99247 | -45.92698 | 2026-08-25 04:08:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e4f1893-ff21-3863-97a3-e462397e4280 | -12.699 | -48.40588 | 2026-08-25 04:08:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f66bd95-9f0a-309e-92f2-35cf3edb0b9b | -7.89639 | -46.38425 | 2026-08-25 04:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 40d8fe52-019c-379c-bde0-e7386a23b615 | -11.58449 | -46.75743 | 2026-08-25 04:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1e62153-a76b-3943-b118-87cb776a6c6b | -12.76716 | -48.36723 | 2026-08-25 04:08:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06146450-cbae-3b21-bd5b-85f9658c6a83 | -10.91328 | -51.07524 | 2026-08-25 04:08:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b4dfaba6-989e-36f4-97e5-5590e6c6b916 | -10.87195 | -50.58313 | 2026-08-25 04:08:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f690178e-c101-3c49-82de-9ea45816fd82 | -10.30985 | -48.20486 | 2026-08-25 04:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 607b7a87-427b-367a-89e0-5b6683788acb | -12.60493 | -44.63594 | 2026-08-25 04:08:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cdca3364-3524-30df-bee3-6347d02d21f2 | -12.70267 | -48.4142 | 2026-08-25 04:08:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce5bddfb-2588-33ce-a97c-ba964388b35c | -9.36559 | -45.41179 | 2026-08-25 04:08:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e74ec91-a1be-3424-9932-49672b07ca80 | -11.77626 | -47.24228 | 2026-08-25 04:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b50f03a3-a316-3edb-b06c-d15dc91eb445 | -11.43181 | -44.53065 | 2026-08-25 04:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1c2f812c-13c4-36ea-a329-28440b5be72a | -7.73644 | -46.15532 | 2026-08-25 04:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f307d125-ee66-3ad7-9c5d-10863249a57a | -12.14259 | -50.60632 | 2026-08-25 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fb55e3bf-82b5-31f2-be21-2e2ba5956601 | -9.63978 | -48.32928 | 2026-08-25 04:08:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1e40769b-22db-3a8b-8887-aea6253968c3 | -14.45343 | -44.29596 | 2026-08-25 04:08:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c4fa7706-db51-33ad-ac26-59f0f9fbf13e | -7.8968 | -46.38765 | 2026-08-25 04:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9dea722c-937d-3661-b366-cacf738ea134 | -11.77524 | -47.27402 | 2026-08-25 04:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2a19eb7e-6fbe-34a8-9368-71e32cf4d1db | -7.90332 | -46.37851 | 2026-08-25 04:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 95071228-cc14-347f-8540-b7ac8999fb2c | -9.94377 | -48.3432 | 2026-08-25 04:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 313e303a-e09c-3a27-b7f4-c4870d5d9ce8 | -8.5692 | -47.4371 | 2026-08-25 04:08:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dea05d77-c6ce-3182-8591-0dc99858244c | -14.79106 | -48.7659 | 2026-08-25 04:08:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 72ba9213-fe2f-3e0d-b1d4-e3c1f878a82a | -9.97372 | -48.32887 | 2026-08-25 04:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f29352b-7b47-3f8e-a0b9-417e585c2f67 | -7.73624 | -46.15384 | 2026-08-25 04:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 573f3b0e-1f6e-3050-8064-37d2dda797b8 | -9.57162 | -49.22968 | 2026-08-25 04:08:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff966a3a-81be-3662-aeb3-3d315173acaa | -8.1151 | -47.48035 | 2026-08-25 04:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8a028fb-3068-376e-9706-7dafbe5f604c | -12.716 | -48.38913 | 2026-08-25 04:08:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ae059b10-b884-3477-b64b-bbb42db29078 | -12.74063 | -46.47478 | 2026-08-25 04:08:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a74e378c-dbd1-3939-a458-a1459d360caa | -12.13118 | -45.12099 | 2026-08-25 04:08:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ca92a85-e854-3926-9735-933b7639ba73 | -11.99525 | -45.93615 | 2026-08-25 04:08:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 4f3f65c9-8b01-3b18-ad41-9e93c1457156 | -11.98818 | -45.9189 | 2026-08-25 04:08:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6a88098a-bd92-3022-94cb-5ab0aee986c9 | -11.38708 | -45.15617 | 2026-08-25 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 574c08cc-54c0-3e27-8399-4d38c8e5b0be | -11.43305 | -44.54712 | 2026-08-25 04:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15c475bd-4d34-3436-be79-845a890d52dc | -8.11565 | -47.47727 | 2026-08-25 04:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1cf72ec8-3bd4-3e34-b7d5-73396674d3f1 | -11.43397 | -44.54186 | 2026-08-25 04:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 043e8ac3-78de-37a9-9411-c47e2ab831f0 | -12.71655 | -48.38632 | 2026-08-25 04:08:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5e8fbcf-f5ef-3fd3-b377-e65a56b61f82 | -9.9686 | -48.32709 | 2026-08-25 04:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11a82554-9877-3e48-8b9f-2ef67dedcc43 | -15.53151 | -40.8554 | 2026-08-25 04:08:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |


[Clique aqui para ver as próximas entradas](README24.md)
