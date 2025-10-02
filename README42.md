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
| 912558c7-62fa-3830-8b16-76313aa63f2d | -12.49798 | -50.25937 | 2025-10-02 04:04:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0b956ca9-2c8b-3223-a8a1-766d16612e03 | -13.0801 | -46.99838 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89b9c9bb-1dd8-308d-9f29-45235ed18ad1 | -15.99469 | -50.91014 | 2025-10-02 04:04:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| f90d375e-d5d5-384b-9ef8-ef5123dd0a36 | -15.14199 | -48.01991 | 2025-10-02 04:04:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5a5764c5-c204-398f-94e5-2c82f03143e7 | -12.68251 | -48.56198 | 2025-10-02 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1ba482c0-f93d-3d24-9fc5-71bb6226da42 | -12.70476 | -48.56953 | 2025-10-02 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7097ac39-0d1a-32c2-b794-065a4699c58f | -13.32149 | -47.21613 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 74714388-ffdb-3c78-9835-9bb57a62b62d | -15.35334 | -46.28612 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc780e77-c19a-30e1-9148-8288d783a61d | -12.68345 | -48.55681 | 2025-10-02 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ef91c094-6ee2-3ed3-b115-d3a725a65f6b | -20.12008 | -44.37931 | 2025-10-02 04:04:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 24ace2fa-aee4-3e8a-9e9b-a17b7affb7c7 | -13.78106 | -48.0554 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3dbedb3e-b155-377b-a74e-a58c1d4e340c | -14.72085 | -41.07145 | 2025-10-02 04:04:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| da3ff37f-1b41-3a0c-b0c0-a376a36048b1 | -20.28565 | -49.23777 | 2025-10-02 04:04:00 | NOAA-21 | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c74088b-1b71-39d7-8b5c-2a4d30a30fde | -17.16703 | -47.02347 | 2025-10-02 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a0badd0c-5199-30d1-aed1-1777ba059e30 | -18.84774 | -43.14318 | 2025-10-02 04:04:00 | NOAA-21 | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 5c82f186-10e0-3ac5-beec-d2dcbe73fb7c | -13.1738 | -47.80993 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 473e16e6-526a-34e9-a7d7-ea96d12825b7 | -13.75059 | -48.0012 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8f50dc3a-7ece-30f5-b149-b4f6a09afca9 | -14.34189 | -43.83704 | 2025-10-02 04:04:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 836ce4bd-1c0e-3964-9baf-be53f1be4bbb | -15.26611 | -49.30614 | 2025-10-02 04:04:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 62842a81-36a6-38ab-978f-ea55c398ae77 | -16.29346 | -46.26191 | 2025-10-02 04:04:00 | NOAA-21 | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4a3baa5-6c5b-3d6f-b217-7c4e6c55b86f | -18.11962 | -42.73271 | 2025-10-02 04:04:00 | NOAA-21 | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7a67746a-642a-3722-b352-0176e3539051 | -15.2898 | -47.9513 | 2025-10-02 04:04:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71a0d422-3be5-32c6-a48d-051db8b5cbe4 | -15.84406 | -46.24135 | 2025-10-02 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fff42230-e654-3d30-8ab7-ce4bd33d132d | -12.94479 | -48.42804 | 2025-10-02 04:04:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| b5f87aa1-1222-3e2d-b8bd-86e4a756d9fa | -20.21387 | -44.18192 | 2025-10-02 04:04:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 61390d3f-7519-3532-8c2e-936a987e0679 | -15.20654 | -48.00176 | 2025-10-02 04:04:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cb3050fe-f0c4-3af3-8ac8-aa7487d73951 | -13.23127 | -48.51098 | 2025-10-02 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| aac11d58-b69b-388e-9ef6-34046e9fee55 | -13.17969 | -47.80217 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7c0ab178-8c77-314d-b28a-3f3bdc891a35 | -15.31302 | -46.29322 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1a34c381-ec7d-3f51-9377-f4326af0a651 | -19.949 | -43.66849 | 2025-10-02 04:04:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 96680374-fb11-30ee-8890-90d92d619c91 | -19.86226 | -42.59169 | 2025-10-02 04:04:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ea52d57a-5221-38cd-92f5-64f25cc58a28 | -17.17379 | -47.03005 | 2025-10-02 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e639898b-e0cc-308a-9db3-30891aa47dc4 | -13.91557 | -48.07066 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6be7ad96-8adb-3267-bc88-7bcdd67de7cc | -19.46437 | -43.65494 | 2025-10-02 04:04:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d5c739c7-58f8-33ba-a7e4-38a2ad9274d1 | -20.74051 | -43.31047 | 2025-10-02 04:04:00 | NOAA-21 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a4ab1da7-1df2-3e9b-9c65-fbb9a2d2d66c | -15.32237 | -46.3951 | 2025-10-02 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a61b54c6-ed73-3123-a780-9d1e3bd8915c | -13.52274 | -47.26173 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 31d09584-f00e-33de-8ca0-46c8d7c6ecf0 | -15.61026 | -46.52832 | 2025-10-02 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36e404fd-13b8-3c57-b175-d0711a113fc2 | -14.41859 | -46.12937 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4b0e6c9-7cfa-3ec2-a387-c3a6b9d813a6 | -14.90885 | -48.3191 | 2025-10-02 04:04:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9dfbb7ba-c64b-37d2-a3b8-4963f0154155 | -13.77535 | -43.62455 | 2025-10-02 04:04:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a41e8a70-d394-3acd-a94a-67b6ccada8e4 | -13.36655 | -46.63016 | 2025-10-02 04:04:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 00641d27-de9a-3763-af18-aa768e3d59b6 | -13.12837 | -47.41528 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5335e7e2-4685-3fe9-9c83-e7d1203deae5 | -13.36465 | -46.33929 | 2025-10-02 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ebb86f46-1bfe-3c58-8868-806c34190fef | -12.57138 | -49.89201 | 2025-10-02 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b61dbafa-13e6-3bb8-933a-4406701890a5 | -15.42895 | -42.76609 | 2025-10-02 04:04:00 | NOAA-21 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c1ded53a-616d-36b6-ae15-6f7468852471 | -13.17814 | -47.81054 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 087b102c-8807-32e7-a30a-fff66111beca | -13.66261 | -48.08903 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b647a93d-3685-31f7-9c41-75eadb870101 | -13.23809 | -47.3373 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 715a46b1-1e19-3e35-9de1-8556c2401a46 | -13.16072 | -47.83238 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c2ecb632-6410-3a96-9266-ff70a12adf69 | -16.00441 | -50.91382 | 2025-10-02 04:04:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e80ba69-a615-3a40-97bd-64ffa5dc5b3d | -15.22839 | -48.728 | 2025-10-02 04:04:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a8cf2bf0-034b-36d2-adca-c38996b0391b | -14.90616 | -47.21752 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd843a0d-b63c-3464-a4f2-29fd22c124c0 | -19.89144 | -42.62302 | 2025-10-02 04:04:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 65dae9a4-97ca-3f0b-a9de-c444254a1a46 | -14.65183 | -48.26361 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 789b4f0c-8c22-37a5-94cd-bbdfccacbfe5 | -12.5708 | -49.89502 | 2025-10-02 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a30a32e-6c6b-3d7c-8260-6b373788c37d | -12.91037 | -47.17299 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 60aa900b-b74a-3a09-b6c4-c17dd7091150 | -13.05356 | -47.00501 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c186070-bb9b-3ba8-bce4-5c36578051df | -19.36391 | -44.25249 | 2025-10-02 04:04:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 793fe942-8c10-3877-b2c9-65732c9d62d6 | -13.15872 | -47.83302 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6aa4c681-89ff-3bd9-9e3d-23c8a77760e5 | -14.02942 | -47.99591 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5fbb41a2-dbaa-338c-a969-177b1695b9c9 | -14.49031 | -48.42387 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 525e7cac-aaf3-3cdc-854d-c086a15dd270 | -14.36716 | -45.95444 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 57ba265d-d182-322f-bfe6-68314a9a8cb2 | -12.71019 | -48.59191 | 2025-10-02 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| db7a0787-fed5-3e3a-bce1-3f2c508e6c49 | -13.97238 | -44.87086 | 2025-10-02 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f71359df-1e8b-3036-ad42-f788b4d170f7 | -13.40973 | -47.78531 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| dade5d40-b5f2-335b-a956-6408420d230b | -12.66615 | -48.57386 | 2025-10-02 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a1e8ff1b-c012-3875-929e-9921c336f204 | -13.75866 | -48.70438 | 2025-10-02 04:04:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1cc5f217-db87-3442-a12d-594daf4c9869 | -16.00384 | -50.86441 | 2025-10-02 04:04:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 98bad963-2034-3cb3-9716-663a40d864a2 | -13.31396 | -47.859 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 55624c5f-d2dc-33fe-a303-8e2bd34a6465 | -14.90185 | -48.30848 | 2025-10-02 04:04:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b258663-7b1b-3886-a666-2c9cff248d8f | -20.62047 | -45.98422 | 2025-10-02 04:04:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c56a9fa7-5dd1-381b-984b-7dfca84f5e1b | -18.66898 | -43.87688 | 2025-10-02 04:04:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 43079708-abec-39e3-b528-c2208f7a19c9 | -13.30776 | -47.19762 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a08f1942-f84d-3dd4-baf1-f8fca9cc697c | -15.22008 | -47.17515 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 88a868a8-4d9a-3165-8ae0-a2b39afb7eb7 | -12.91108 | -47.16906 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dd7577b2-662d-3b01-85f6-04c3485c86b9 | -19.46106 | -43.65437 | 2025-10-02 04:04:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7a94a13-4ecc-339d-b7ac-0eba75b13822 | -13.69867 | -48.62462 | 2025-10-02 04:04:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a4011a05-3dda-3a8e-9135-3dcffab07980 | -18.60703 | -50.69613 | 2025-10-02 04:04:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1c8420ec-082e-3804-a5cf-5502496152de | -13.2079 | -48.51122 | 2025-10-02 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 31410d96-2189-384a-a981-81cc210bbdec | -19.95854 | -43.65125 | 2025-10-02 04:04:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 63f02037-478e-31a8-9bb1-3d0556694fcd | -13.16883 | -47.82631 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d85a146e-8f48-3865-be7e-b5dd0d3eab8a | -14.79807 | -44.88803 | 2025-10-02 04:04:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 292e3849-ad91-32a8-a6b3-cfc26a30da3d | -13.34227 | -47.80119 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8022117-e17b-3479-8718-1434c0c27ca9 | -14.91041 | -47.22202 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d40418b3-7470-3adf-bea6-0180e882fbbf | -16.28411 | -42.54739 | 2025-10-02 04:04:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b291c944-cf0a-3bff-80c7-7b2dee8075ef | -15.56098 | -48.18494 | 2025-10-02 04:04:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43774454-bd4a-3bb3-b5bd-ec40f7031001 | -18.52498 | -45.04031 | 2025-10-02 04:04:00 | NOAA-21 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3084b236-2b20-37cf-8fd7-72ef88b1fe9a | -13.16286 | -47.82082 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c945a958-318a-3465-9467-e32ea60a157d | -13.31993 | -47.20111 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4e40eb32-f99b-3fbc-a905-ef5cc4ca4d8c | -19.84781 | -44.08581 | 2025-10-02 04:04:00 | NOAA-21 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ee472358-9d63-3b7a-95c7-0cf51803a166 | -16.50139 | -46.94881 | 2025-10-02 04:04:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db018e04-f097-3937-ab49-c333ea4af833 | -13.57662 | -47.5896 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5671d78f-8566-393f-9ef3-d466e8859a3f | -17.07498 | -44.9115 | 2025-10-02 04:04:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dfa28e35-18a4-3915-beb2-40fcbc37b438 | -13.15933 | -47.82963 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b0f5ce08-6264-3ee5-8025-2cbf3d295175 | -14.62165 | -48.3051 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 31bea156-3403-31a5-be63-9d5ae798252b | -17.07567 | -44.90749 | 2025-10-02 04:04:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 18d4016c-ff6f-37cf-a70a-1c794c0efa19 | -14.3168 | -45.88691 | 2025-10-02 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 930d9bf4-2c86-35f5-9b8e-979dcea8ebdd | -13.15151 | -47.84842 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c16caf26-56ab-318c-a9c6-7ec72892db33 | -13.31482 | -46.99531 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README43.md)
