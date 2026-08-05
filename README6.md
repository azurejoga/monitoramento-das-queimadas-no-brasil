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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f96b25ac-10f0-3212-a0eb-661c2cc3e2be | -8.3521 | -45.98563 | 2026-08-05 03:42:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e2a61e6f-5060-33ee-a62f-d65e391516ce | -11.51887 | -43.24826 | 2026-08-05 03:42:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6d25f87b-88ad-39d0-b3ff-0b405a30720c | -12.58434 | -46.95164 | 2026-08-05 03:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b9a1cc59-0bbd-37af-92b8-02135487e0aa | -12.58979 | -46.95947 | 2026-08-05 03:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5710c709-6fda-3902-b0f4-a2a417dcf0f0 | -11.30129 | -44.79866 | 2026-08-05 03:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 45aaed58-1f4d-350e-a875-a04b9dae39d2 | -9.4807 | -40.36889 | 2026-08-05 03:42:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fcff2fe4-5249-3f6a-ac91-7c0b44fda784 | -12.5986 | -46.91742 | 2026-08-05 03:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5d74ed5b-fe17-3a50-93d4-f3fedf7b9594 | -11.5244 | -43.24938 | 2026-08-05 03:42:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d7c2036f-9cf0-3db5-90d3-c4a91b6899db | -7.22119 | -43.34988 | 2026-08-05 03:42:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dd518bb4-319d-33cf-a2a4-7caca9523b58 | -8.35081 | -45.99219 | 2026-08-05 03:42:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 14ac433f-4aed-3469-883e-6a3a230d0447 | -12.59582 | -46.9341 | 2026-08-05 03:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 48c78668-fbf2-3dbd-9115-5a53a3306d94 | -11.5542 | -47.71586 | 2026-08-05 03:42:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d3a6856-459e-3a6b-aebe-000733de3a31 | -7.22456 | -43.35494 | 2026-08-05 03:42:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d5741abe-ec4c-3da8-8294-10cb7be07b07 | -7.22716 | -43.35109 | 2026-08-05 03:42:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 318e660c-a201-36d0-9ad9-77aa28be4434 | -12.58499 | -46.9514 | 2026-08-05 03:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fddbeb26-10f5-3ba3-ac0d-27700437acb2 | -12.59044 | -46.92262 | 2026-08-05 03:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 017d816c-e06f-3ab6-b685-d255869d96e2 | -10.60593 | -46.38428 | 2026-08-05 03:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e4960266-96c2-3763-8b80-8fa906e881f2 | -12.58297 | -46.95816 | 2026-08-05 03:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b1458040-a0e6-3498-bb0f-f63fd2e6c3a1 | -11.51816 | -43.25197 | 2026-08-05 03:42:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 54feda87-bd18-3df0-a327-4b35284ffb27 | -12.5881 | -46.93375 | 2026-08-05 03:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d7bdcdab-d000-336f-b49d-9474744dc650 | -12.59 | -46.9283 | 2026-08-05 03:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 705d3012-659e-35cd-8694-6180d7aa87f9 | -10.61405 | -46.37918 | 2026-08-05 03:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b82684e6-d9af-363e-8299-18c02f2050b5 | -12.59446 | -46.9404 | 2026-08-05 03:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 53868a76-2cc5-31b7-9d64-8affe0dfd1b2 | -8.35338 | -45.97911 | 2026-08-05 03:42:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7ae67f34-ed73-32cb-825e-e7b40fe29676 | -12.59506 | -46.93427 | 2026-08-05 03:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a769b657-d75b-3f66-b265-c13fe0c8cc2f | -12.591 | -46.95369 | 2026-08-05 03:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2c648000-2922-3155-9f8b-a670ff49d3b8 | -12.58921 | -46.92848 | 2026-08-05 03:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1db559d2-0a9f-3891-8fa0-ed8c7147bfbe | -7.62248 | -45.317 | 2026-08-05 03:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e7d02f33-57f8-30b0-8966-c0197d5cf7f3 | -12.59125 | -46.92251 | 2026-08-05 03:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2156c7b-a511-31c3-8642-347992d107b3 | -11.04083 | -42.75332 | 2026-08-05 03:42:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 52a93560-abc2-3971-8361-69a15464d8f3 | -12.59293 | -46.9475 | 2026-08-05 03:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e14b4429-494f-3ac2-ba4a-118a12f5b8a6 | -12.59034 | -46.95945 | 2026-08-05 03:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 283d0353-c782-33f8-b978-123d86c85689 | -12.59175 | -44.162 | 2026-08-05 03:42:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0350eef-fe1b-3dcb-b490-d6fc368fe5ed | -12.59704 | -46.92847 | 2026-08-05 03:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c442a8df-11da-3d02-9d90-6c56a025242c | -9.48531 | -40.36785 | 2026-08-05 03:42:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8c223438-b7d1-3298-89c3-269944891d20 | -7.62368 | -45.31078 | 2026-08-05 03:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6af7bfd-d951-39a9-ae5b-58a4d418a3cb | -12.58192 | -46.93289 | 2026-08-05 03:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23d8c25f-7ee6-3c50-a3eb-7179148d8f9d | -11.30037 | -44.80331 | 2026-08-05 03:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c9505bc1-77c9-3d88-8043-545f0fa40e5c | -12.5857 | -46.94515 | 2026-08-05 03:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 18445d8f-0fa9-3c32-bb98-1a09fe33ceba | -12.59229 | -46.94752 | 2026-08-05 03:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 50b89963-c742-36ba-9cac-54daf4ab579b | -12.58118 | -46.93298 | 2026-08-05 03:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| a587ceda-c333-3937-87d8-11f03b87dee7 | -9.09129 | -37.66281 | 2026-08-05 03:42:00 | NPP-375D | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9a2c75ba-7244-33a8-bba2-f9eacd10db22 | -10.63677 | -47.4862 | 2026-08-05 03:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9b205544-490b-3f87-aba1-a2c86078a6ee | -9.48441 | -40.37299 | 2026-08-05 03:42:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0bc85eaf-a501-3169-9492-01d870c539ab | -12.59623 | -46.92873 | 2026-08-05 03:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d9859c1b-e7c3-3ee1-83f9-9ef8f9c306af | -12.58359 | -46.95788 | 2026-08-05 03:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| aaf8bc32-6cb8-30b1-995a-e6fad2eee9c7 | -12.59823 | -46.92298 | 2026-08-05 03:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c5518bc-0df7-32d3-a31d-fb031222442a | -9.47975 | -40.37401 | 2026-08-05 03:42:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 85b86db1-9da7-3abc-9042-af37e7b041a5 | -11.04623 | -42.7544 | 2026-08-05 03:42:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 66376652-3b94-3e9c-86e4-d7e88b48b54c | -10.13858 | -46.37214 | 2026-08-05 03:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0500748d-e764-304b-84bd-3780c9825501 | -8.33828 | -45.98317 | 2026-08-05 03:42:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac3d8cc4-23df-3b26-98d9-2341b8fff5c9 | -12.59159 | -46.95369 | 2026-08-05 03:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dc7e3c36-efd5-3af1-9a10-4818c88a34ad | -7.6304 | -45.31197 | 2026-08-05 03:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5408b2c2-bc84-383a-bca2-664e47d236c7 | -12.5917 | -46.9166 | 2026-08-05 03:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fb5c9ebb-680f-3553-8285-3f3c61605058 | -10.63528 | -47.49316 | 2026-08-05 03:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 376a85f4-28d1-381a-a157-cc23a86ec724 | -12.59375 | -46.94053 | 2026-08-05 03:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 66855d96-ec9c-375e-a792-cdd7a4c5a533 | -12.58885 | -46.9336 | 2026-08-05 03:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bd17228f-1026-3b64-b1a1-c7491c88990c | -10.61275 | -46.38553 | 2026-08-05 03:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 38743ae8-e010-3e69-b56b-17174a2c92c4 | -11.51746 | -43.24942 | 2026-08-05 03:42:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| a1ba935c-3b71-36c7-a0b0-873a2dadd57a | -12.58638 | -46.945 | 2026-08-05 03:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0df02a32-4d0c-34c8-9e11-a50a74a879df | -12.49418 | -45.54581 | 2026-08-05 03:42:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8b8efade-4f8a-3092-9d6b-9c90b9316793 | -12.59948 | -46.91721 | 2026-08-05 03:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2632e193-06da-3bf4-a1a4-fbcf7b0f1306 | -18.35623 | -39.79767 | 2026-08-05 03:45:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ebcea2de-a583-3615-a0a0-dbf1e4a8db22 | -17.983 | -47.16397 | 2026-08-05 03:45:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 713a01a0-de4f-340d-aed9-ec9204ebbe60 | -18.35136 | -39.80212 | 2026-08-05 03:45:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| c71e9955-781f-3fe1-9f2c-3b41350fbcb7 | -15.44378 | -41.37948 | 2026-08-05 03:45:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e94deba3-0c54-3cf8-b775-781b2e3f2721 | -14.26819 | -45.29932 | 2026-08-05 03:45:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14f6d76a-94b5-39a2-95e6-74cf5d38d855 | -15.44726 | -41.38213 | 2026-08-05 03:45:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 618090e2-a3cb-32d3-b695-c35a2fd43865 | -13.44361 | -43.67647 | 2026-08-05 03:45:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| ae92bd6d-859b-38a6-bfda-01dc899a29af | -21.49981 | -41.2534 | 2026-08-05 03:45:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 664743a8-6b38-361d-a190-b1abff59af70 | -17.9915 | -47.15534 | 2026-08-05 03:45:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5f07c27f-6eb3-3f88-976c-350253cbb8c4 | -20.88601 | -42.77956 | 2026-08-05 03:45:00 | NPP-375D | SÃO GERALDO | MINAS GERAIS | Brasil | 3161502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d6a8cbba-7e1f-35de-a7db-1321c696e0d1 | -13.43648 | -43.85746 | 2026-08-05 03:45:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bbcb2670-b24a-3c91-9ad8-ff06120dd4c6 | -19.79315 | -46.04795 | 2026-08-05 03:45:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4b9bf694-c7ca-33e0-8af9-fc81e71a9b16 | -18.46275 | -43.25289 | 2026-08-05 03:45:00 | NPP-375D | SANTO ANTÔNIO DO ITAMBÉ | MINAS GERAIS | Brasil | 3160207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 757a89d9-3a40-3c20-9aef-84a251797bbf | -14.26222 | -45.298 | 2026-08-05 03:45:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81c1b181-71e8-3c95-944e-a675a947df18 | -15.43831 | -41.38342 | 2026-08-05 03:45:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 54dee185-050e-3a03-b512-e1c021c97cf4 | -18.69638 | -44.5501 | 2026-08-05 03:45:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61d3e255-ca2d-35c9-84e5-b17898e6623c | -13.43813 | -43.67528 | 2026-08-05 03:45:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 3e6cdee3-6bc7-3e86-b13a-ab69de351bc1 | -13.44036 | -43.85627 | 2026-08-05 03:45:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04941b8d-94ee-38c8-bf23-5bc000ab3da5 | -17.33624 | -42.63028 | 2026-08-05 03:45:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2f60c42b-4e13-3638-b87e-6fdaed950dba | -13.43091 | -43.85636 | 2026-08-05 03:45:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9dbcf475-ab22-3516-8c0e-275cab6a6fd9 | -19.794 | -46.04419 | 2026-08-05 03:45:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 59f2d7c3-fee9-3d52-bef3-bec73d5316d9 | -13.43243 | -43.84872 | 2026-08-05 03:45:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e67a4ea4-8933-315c-921d-f62b81d273fa | -13.43798 | -43.84983 | 2026-08-05 03:45:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e829eb6-f4ca-3e58-8f26-11d3475f3990 | -18.3544 | -39.79964 | 2026-08-05 03:45:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 68d401b9-5367-3a9b-9e69-1391717fb824 | -15.44831 | -41.38058 | 2026-08-05 03:45:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2a6c0434-ea09-3fd1-b564-bdd675e998c3 | -19.98393 | -42.28075 | 2026-08-05 03:45:00 | NPP-375D | VERMELHO NOVO | MINAS GERAIS | Brasil | 3171154 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9ab43a22-fb6f-3f01-bf4b-7e866524636d | -15.44285 | -41.38444 | 2026-08-05 03:45:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e8d2e6a0-6577-3961-8a73-acd43fdce3bd | -17.33515 | -42.63574 | 2026-08-05 03:45:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 76a8542a-4af2-3701-a9a5-36334953fdb5 | -18.35232 | -39.79683 | 2026-08-05 03:45:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7b11c450-2745-3014-9cb5-f3b1939ffe17 | -15.44274 | -41.38106 | 2026-08-05 03:45:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 8775f6a4-079e-3e38-a427-88df8bc010c4 | -13.43723 | -43.85367 | 2026-08-05 03:45:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06ce4295-00c1-3fe1-ba38-633e66ab02d2 | -13.43167 | -43.85255 | 2026-08-05 03:45:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 318fd21c-e98b-33a6-8181-8f98e41c11b9 | -14.26126 | -45.30257 | 2026-08-05 03:45:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5da5e01-0716-34cc-9491-3d929932168a | -13.43016 | -43.86015 | 2026-08-05 03:45:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c227132-b570-3f55-959d-2401af4e3372 | -20.88498 | -42.78466 | 2026-08-05 03:45:00 | NPP-375D | SÃO GERALDO | MINAS GERAIS | Brasil | 3161502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 57b475db-a9a3-3855-af52-182a6b22bc60 | -13.44113 | -43.85252 | 2026-08-05 03:45:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 392cb296-4526-33fe-91f5-ff94609142d5 | -18.35048 | -39.79883 | 2026-08-05 03:45:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 98d63178-a7f9-3303-bea6-a4265d339788 | -17.33991 | -42.63683 | 2026-08-05 03:45:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |


[Clique aqui para ver as próximas entradas](README7.md)
