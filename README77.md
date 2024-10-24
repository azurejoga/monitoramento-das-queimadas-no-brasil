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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d03194af-c920-367d-9a06-d86d61acb91f | -11.60342 | -48.54309 | 2024-10-24 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6c729949-016a-3bcc-a30d-93dddf380dc2 | -11.6028 | -48.54768 | 2024-10-24 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a3963dc4-eafe-3c79-8f90-665865c08e53 | -11.60113 | -48.59383 | 2024-10-24 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1391d087-3d2f-3a83-a0d5-f809cb8d66af | -11.60106 | -48.45776 | 2024-10-24 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50cc43f0-1ce3-3e63-8e9f-47e9fa3a955e | -11.59935 | -48.50486 | 2024-10-24 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94f3d1eb-ac92-3252-a9eb-a5aaee581ec5 | -11.59765 | -48.55164 | 2024-10-24 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2704a6f3-d6d1-39c7-8f23-ce0643571f05 | -11.59703 | -48.55623 | 2024-10-24 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f873fa50-bf9c-31e9-b427-496cf0595b44 | -11.59662 | -48.5932 | 2024-10-24 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d636cc7d-067a-327a-ac31-ed7f17db8a16 | -11.596 | -48.59774 | 2024-10-24 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04f44a54-1b43-3e4e-b30a-c657673debf4 | -11.59481 | -48.50423 | 2024-10-24 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 705f7570-1905-33b0-b138-d86d657493e8 | -11.59313 | -48.55101 | 2024-10-24 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9e3f72f4-dcc5-31ff-9d0c-8f77055ced13 | -11.59251 | -48.55561 | 2024-10-24 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c3ddfc7f-331d-32e6-a1bb-3c34071624b4 | -11.59211 | -48.59255 | 2024-10-24 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b659c9f-d423-3699-b81a-a05ba871f499 | -11.57566 | -48.54381 | 2024-10-24 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dd5478d8-a47e-3404-b2e3-875941bb1804 | -11.57114 | -48.54317 | 2024-10-24 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e79d98fc-337c-370b-9d2a-41505f2d4ef6 | -11.25377 | -48.7159 | 2024-10-24 04:57:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1415831e-d5af-374c-a8b0-1c0b9375592d | -11.25317 | -48.72029 | 2024-10-24 04:57:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c950a7b4-0a65-332a-aa3a-1ebb48a3fe63 | -11.235 | -48.44688 | 2024-10-24 04:57:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0e649754-53e6-3024-a9eb-f1895bf99e0d | -11.11867 | -48.62235 | 2024-10-24 04:57:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d0353a7-64ff-3259-bd60-84cd119d88b4 | -11.03005 | -48.27551 | 2024-10-24 04:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 160edf74-cfe5-316a-8eb9-c5cff9c986fd | -11.02942 | -48.27717 | 2024-10-24 04:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 152e169b-1b55-3bb5-9379-3da9064aebef | -11.02548 | -48.27486 | 2024-10-24 04:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dacbbcc9-680b-3fb3-842c-30c659fdd0ea | -11.02485 | -48.27652 | 2024-10-24 04:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 445db241-f6db-37b2-a9c3-65c8e87f9530 | -11.02482 | -48.27961 | 2024-10-24 04:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 30daa6cb-71ac-31ce-91bc-b43cf0b2be14 | -11.02422 | -48.28131 | 2024-10-24 04:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f5553c11-7fb1-3fe3-ade7-02f703ab6d5f | -11.0209 | -48.27425 | 2024-10-24 04:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 54ea9968-4d6d-3ddd-baa6-b5ee243b181a | -11.02027 | -48.27589 | 2024-10-24 04:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5f67a72a-adff-323e-8487-620c3a997e75 | -11.02025 | -48.27897 | 2024-10-24 04:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 24e2845b-c93c-3c6d-94ce-f106e4f9957c | -10.89885 | -48.66445 | 2024-10-24 04:57:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c067a10d-84b8-36d1-87e1-246d9c468e92 | -10.89441 | -48.66378 | 2024-10-24 04:57:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1bc7d942-5066-32a8-a7eb-fbc57e73c273 | -12.05482 | -48.33583 | 2024-10-24 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ea7f156c-d2de-36da-b570-c9d8e91423e2 | -12.00751 | -48.26525 | 2024-10-24 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 986e24a4-3ee0-3a61-ad86-ab200a8b207e | -12.00687 | -48.27019 | 2024-10-24 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 45a73120-3067-3cf8-9640-1c68236bb669 | -12.00287 | -48.26463 | 2024-10-24 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3651bda8-eff2-324e-b80a-39b1d0fca848 | -11.99127 | -48.46257 | 2024-10-24 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3407f050-4391-3532-bf73-ea0ac3b10225 | -10.87806 | -49.14156 | 2024-10-24 04:57:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 914cdad2-5be5-33eb-b870-2a2fbb7340b1 | -10.87749 | -49.14563 | 2024-10-24 04:57:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c88df1c1-8cd5-39c2-959e-50787d59bff9 | -13.27431 | -49.2487 | 2024-10-24 04:57:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8525bb58-fab7-3321-8201-ad6eaf95d2f6 | -13.10382 | -49.12452 | 2024-10-24 04:57:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c839e93-09de-3bfc-8386-4217046d1bf2 | -13.00476 | -48.88939 | 2024-10-24 04:57:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d43ee2e6-0c16-3de0-b434-f2a2ff86963a | -13.00025 | -48.88874 | 2024-10-24 04:57:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 656d4fc2-2f0e-344c-be93-fbe5c5300dd7 | -12.9695 | -48.94985 | 2024-10-24 04:57:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eeedcf6c-8f1c-3bc9-8fea-3d96a1ac38bc | -12.95926 | -48.87212 | 2024-10-24 04:57:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6b768a2c-dea6-3ac4-8e48-74f84dce920b | -12.95475 | -48.87149 | 2024-10-24 04:57:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cd51bea9-c592-3cce-bcf1-86c4f3c2c306 | -13.01517 | -49.56155 | 2024-10-24 04:57:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3756fba6-cf28-33d1-8986-397a3134ac8b | -13.01085 | -49.56097 | 2024-10-24 04:57:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4cb7d037-2fa5-3033-8005-3a42219091ad | -12.8907 | -48.5137 | 2024-10-24 04:57:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1f92360a-ff84-3cbf-9298-702ebf43237e | -12.89008 | -48.51839 | 2024-10-24 04:57:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7740c6d5-b771-36f1-806b-47276e019d9d | -12.88609 | -48.51301 | 2024-10-24 04:57:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4db6665f-b590-34a8-a8cc-c18bf8a50ad1 | -12.88547 | -48.51768 | 2024-10-24 04:57:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 87424337-b402-3ce5-b07b-71a7a3dac342 | -12.61867 | -49.47967 | 2024-10-24 04:57:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f0ebbb53-05b8-3d45-af9a-a670747754c8 | -12.60571 | -48.52198 | 2024-10-24 04:57:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9471b6e-d1c1-34bb-b5d3-5b7e3afe578f | -12.6057 | -48.52497 | 2024-10-24 04:57:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e79afbb4-8842-3787-aec3-3b945a5d8c6e | -12.60513 | -48.52653 | 2024-10-24 04:57:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f978e4d-fa22-330b-a336-511a639de52c | -12.592 | -48.77244 | 2024-10-24 04:57:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4fabb532-8f54-3f87-9b92-76a5de8eb904 | -12.27083 | -49.45227 | 2024-10-24 04:57:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ef320d6-ce2c-3118-b8bb-52aa0ba42f93 | -14.55837 | -49.72666 | 2024-10-24 04:57:00 | NPP-375D | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb70b95f-60aa-3cdc-8fd4-4c47974bdd77 | -14.55402 | -49.72602 | 2024-10-24 04:57:00 | NPP-375D | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1d8fca4-2058-3d44-9949-c4c241669c1a | -7.82694 | -48.72516 | 2024-10-24 04:57:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a30b5ec-dfb8-3290-94ed-50d9d84a5122 | -7.70511 | -48.85461 | 2024-10-24 04:57:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11d963f2-ddd9-3657-b254-92ba4b87be3b | -7.36172 | -49.58535 | 2024-10-24 04:57:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb027495-a76a-38d8-8272-dd69be73aca3 | -7.17959 | -49.30324 | 2024-10-24 04:57:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac432533-570e-3157-8a70-6a7a032e2f6e | -9.43385 | -48.87957 | 2024-10-24 04:57:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af313b95-51c3-3a5e-8e0b-2c0264e68529 | -9.43326 | -48.88362 | 2024-10-24 04:57:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e51c33c9-080e-31a9-b40d-efd27a84337e | -9.31549 | -49.40749 | 2024-10-24 04:57:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94e82d3f-e373-30e1-a582-86faac782709 | -9.31496 | -49.41121 | 2024-10-24 04:57:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b61015d7-f160-3991-8d79-5c70c831d780 | -9.27096 | -49.57382 | 2024-10-24 04:57:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b710e2f-f35a-3740-8e3a-b45a9f052589 | -9.27044 | -49.57746 | 2024-10-24 04:57:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d7c7c0c-e241-3385-893c-270883650e04 | -9.2704 | -49.63644 | 2024-10-24 04:57:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0ff6493-598b-32c5-ac4a-5db122c80ef2 | -9.26637 | -49.5768 | 2024-10-24 04:57:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23046641-b8d3-38ae-94d7-ade892052413 | -9.1616 | -50.05935 | 2024-10-24 04:57:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02f5448c-706d-36f1-ba26-c325fa0a60c4 | -8.67301 | -49.09242 | 2024-10-24 04:57:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f49ec30-a230-3d97-9dab-b6cc3f4c8c6f | -8.58096 | -49.22252 | 2024-10-24 04:57:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c14ba029-914d-3e40-a2d1-f0262e40c135 | -8.58044 | -49.22622 | 2024-10-24 04:57:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 747a80c4-f7ba-33a0-9a73-420361bb8812 | -8.57736 | -49.21819 | 2024-10-24 04:57:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ed24e87-8a71-3e01-a5e8-3105f70d9497 | -8.57683 | -49.22193 | 2024-10-24 04:57:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4532c24f-de43-3d21-b7d9-590a5451c089 | -8.46682 | -49.53009 | 2024-10-24 04:57:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94b34cd8-e84c-3194-80b6-38b0c5f2badf | -8.39117 | -49.96296 | 2024-10-24 04:57:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e00d99e-87e2-3c56-aa0c-2c768058f20d | -8.39044 | -49.96797 | 2024-10-24 04:57:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb6fa15a-7d75-3790-8903-7908a032111e | -8.38724 | -49.96238 | 2024-10-24 04:57:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0470c8e-928f-34f4-9a46-57678b7adb7a | -8.3865 | -49.96739 | 2024-10-24 04:57:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce8335a2-14b8-3b1c-96c2-0637bcf08c33 | -8.38451 | -48.64759 | 2024-10-24 04:57:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe2cab50-961e-330e-864e-2264f8b52d7c | -8.26025 | -49.4711 | 2024-10-24 04:57:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ade2b7c7-9721-396c-8a29-1d2d75dd8266 | -8.25974 | -49.47462 | 2024-10-24 04:57:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a70ad189-23a2-3dcf-99e4-3ca8d85478d4 | -8.19431 | -49.6699 | 2024-10-24 04:57:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6b835a72-c677-33b3-9182-9e999bfb5de8 | -8.15268 | -49.29746 | 2024-10-24 04:57:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| acb90bff-9811-347c-91be-76775baddf0e | -8.15015 | -49.77901 | 2024-10-24 04:57:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 44230904-b25a-3743-a9cb-b260ce43a241 | -8.09236 | -49.34029 | 2024-10-24 04:57:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5461e6d2-060a-3bbb-bad2-35e1f182e338 | -8.06425 | -48.89973 | 2024-10-24 04:57:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24a3f1d6-d3b0-37dc-8fa1-024300d3d3d8 | -8.06372 | -48.90351 | 2024-10-24 04:57:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2ab62453-7511-342a-b129-7424aad85613 | -8.0628 | -49.37759 | 2024-10-24 04:57:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 60171286-c9ab-385d-897e-fc3e328e9b02 | -8.0582 | -49.38065 | 2024-10-24 04:57:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5d45d80-c50f-3538-97f7-ec991681fa74 | -8.02697 | -49.75767 | 2024-10-24 04:57:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8af99801-c8ae-3221-a31d-b0d2deaa48b8 | -8.02561 | -49.75372 | 2024-10-24 04:57:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b18a8a72-f211-35ad-bdf6-4c5a9035692b | -8.02462 | -49.63659 | 2024-10-24 04:57:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4794b257-4597-3b7c-b25c-6b6eae79307c | -8.02063 | -49.63599 | 2024-10-24 04:57:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 61e947e7-5fdc-3953-a6b6-cedfe2e04f9d | -8.01739 | -49.63025 | 2024-10-24 04:57:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5d4eae32-59c9-3473-8992-e6b65730cfd4 | -7.96841 | -49.45822 | 2024-10-24 04:57:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48dac07a-4195-3fef-9514-d7b76f21d605 | -9.84281 | -49.0426 | 2024-10-24 04:57:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b84fcde8-5a2d-3f99-be3c-19431df8cc9e | -9.84014 | -49.04278 | 2024-10-24 04:57:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README78.md)
