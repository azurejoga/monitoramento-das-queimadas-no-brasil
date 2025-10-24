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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4066b2cc-25e1-3289-b831-bb7764d06736 | -14.77028 | -49.29392 | 2025-10-24 04:19:00 | NPP-375D | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7764062c-8a47-38fc-9255-920b5d3b6a03 | -15.60924 | -45.92082 | 2025-10-24 04:19:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9c5213f-edea-33f9-9e2a-51acdc4c86bd | -12.7754 | -47.37963 | 2025-10-24 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| d8496cf1-415f-3564-86d2-e698c2f2438c | -19.64713 | -47.85982 | 2025-10-24 04:19:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c7857a22-69c1-3343-9e3d-95fb4c258fdf | -6.02057 | -48.90535 | 2025-10-24 04:19:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4751f024-b7a9-392a-a5d1-42c3cb25d556 | -19.53797 | -44.84922 | 2025-10-24 04:19:00 | NPP-375D | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b1420af0-da29-3b6b-bba6-787e6923969d | -18.76114 | -46.82209 | 2025-10-24 04:19:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 63d42084-f686-31c5-bc75-f97d162bdfc8 | -13.30188 | -47.44953 | 2025-10-24 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b006e2c-e33e-3d9f-9ccc-e8417eeae230 | -15.19146 | -47.0847 | 2025-10-24 04:19:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40badff1-7953-3e98-9953-af32f35a987b | -14.04023 | -48.72707 | 2025-10-24 04:19:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8404f3e-771c-3102-86bb-e19eee69fe3c | -15.44581 | -48.57781 | 2025-10-24 04:19:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 49d1ac66-9e84-380e-abaa-8a9f4698deb3 | -14.7422 | -46.60825 | 2025-10-24 04:19:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af7c5470-ce93-33f9-b34a-e7097b421fb1 | -17.59815 | -46.62358 | 2025-10-24 04:19:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 216c4382-e03b-36d0-bb3e-0025a785935e | -17.65334 | -46.65565 | 2025-10-24 04:19:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0c884c5-ec2a-3646-aa27-e0ade4f9ea55 | -8.1557 | -43.39081 | 2025-10-24 04:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 25a009e1-680e-328e-abc1-4f5d11cee635 | -8.20518 | -46.99037 | 2025-10-24 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 0a8c8d02-b6eb-3795-9c7e-83c298b4bfaa | -9.3869 | -40.52017 | 2025-10-24 04:19:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 419fa19c-bd2c-3a66-b32e-aa4591254b73 | -8.12066 | -47.38613 | 2025-10-24 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8ffeed87-c7d3-3da5-9617-5ef46d9fc003 | -13.7332 | -48.37996 | 2025-10-24 04:19:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3808de2d-ad41-3117-bd3d-8bc178638af8 | -15.83819 | -49.09685 | 2025-10-24 04:19:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8ff56429-ca48-3bff-b83c-6d269ae66bb8 | -14.77203 | -44.97189 | 2025-10-24 04:19:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c7fbfb5-cab6-3e52-91ef-a8f870c33435 | -6.11307 | -48.10382 | 2025-10-24 04:19:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4e7a3fac-6dad-39ca-a1f0-15adafbc3d6e | -18.24991 | -44.19249 | 2025-10-24 04:19:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8628faae-5ab5-3ef0-8c41-a226c0702d66 | -14.7462 | -46.60515 | 2025-10-24 04:19:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0184c639-c9d3-3cc2-b831-65c6aca1f3dd | -7.55281 | -47.36174 | 2025-10-24 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| daeecb35-848e-3eff-ac2c-10c9bcfaa364 | -6.43171 | -45.67236 | 2025-10-24 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79924392-72a3-31b6-b119-8751a5393075 | -15.94219 | -51.05581 | 2025-10-24 04:19:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88fea022-982a-3b02-9846-a106bfc8cde6 | -14.38486 | -51.52094 | 2025-10-24 04:19:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| acfe2a39-c44e-3f80-9d7d-93943cdc5d16 | -15.31109 | -46.88966 | 2025-10-24 04:19:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2a68cbe-5064-3569-aff4-475994d769fc | -16.37408 | -47.41761 | 2025-10-24 04:19:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3ee15fae-7bd8-3f0b-82db-be490b9a4c55 | -12.81403 | -48.67171 | 2025-10-24 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d45a3492-d99f-3511-a23b-0b291faffaea | -7.08075 | -46.5205 | 2025-10-24 04:19:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc9a718b-ac1e-3477-bf16-ac1a8a7fcedd | -17.47265 | -45.99205 | 2025-10-24 04:19:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3feb54ea-ddf6-3cd7-8238-3ac17beb3b34 | -8.31892 | -46.25125 | 2025-10-24 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b469a7b-0687-3c0b-85ee-c9e8c75af413 | -16.25104 | -46.7855 | 2025-10-24 04:19:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ceef8f5e-8f1a-304f-8ccb-1df0da86d767 | -19.88917 | -46.95891 | 2025-10-24 04:19:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7ee83d6-7ca4-31e8-bba8-03316581fd3c | -13.26036 | -47.89292 | 2025-10-24 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9efd9bbe-bc0f-36d8-8a00-9a6276e375da | -12.81553 | -47.03224 | 2025-10-24 04:19:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dbe22380-ec08-327d-a977-e4f95edd196a | -8.29921 | -42.30025 | 2025-10-24 04:19:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 774c965a-a285-307c-b54c-0b70e94404b3 | -12.6675 | -48.62646 | 2025-10-24 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8de58fa-cf3a-3c79-961b-d37504b3149b | -14.75637 | -46.60693 | 2025-10-24 04:19:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3c05954-b011-3aed-b66f-c39bf697092d | -12.38865 | -57.52855 | 2025-10-24 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3fcb4123-2d2d-3ae2-9c8a-74d58d96a3fe | -6.97395 | -45.28535 | 2025-10-24 04:19:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 99ca6590-56b3-34f7-9373-0391313a2cb5 | -11.48081 | -54.01496 | 2025-10-24 04:19:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd7f46d4-5f26-35cb-acea-b37237e0561b | -15.60707 | -45.91301 | 2025-10-24 04:19:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 985fa81d-202f-3c11-8331-88847885956e | -14.47923 | -47.91764 | 2025-10-24 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| fcae78ae-efda-3918-b4d9-793655d0df2b | -6.84096 | -42.45678 | 2025-10-24 04:19:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 506fe362-60f1-3376-b6a9-6bb056ba2b45 | -12.81316 | -50.94226 | 2025-10-24 04:19:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1f788adb-6c30-3276-a71c-def46b822ef3 | -7.68866 | -42.23936 | 2025-10-24 04:19:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bb045830-518e-3b04-87c2-f9276abb0675 | -14.436 | -50.94706 | 2025-10-24 04:19:00 | NPP-375D | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 832e7414-730f-3316-b1a0-b087795fef51 | -12.73406 | -46.34468 | 2025-10-24 04:19:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6dc78c92-5930-3733-ae88-b6865b7119f7 | -19.99209 | -44.23053 | 2025-10-24 04:19:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 089794d1-62f5-3d6c-9d70-1c49a9686e0b | -13.90529 | -48.3856 | 2025-10-24 04:19:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6415d371-90de-3982-8b84-7a82673a7e3f | -6.44556 | -47.27588 | 2025-10-24 04:19:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 91e7b83e-78db-34d0-a78e-4f04f7137780 | -15.13015 | -47.93887 | 2025-10-24 04:19:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 23c6a814-bf0d-3456-afb8-d7196df3157c | -13.66442 | -47.95562 | 2025-10-24 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a305d73c-8055-337e-ad91-ee5abe5c88c6 | -14.20491 | -44.6005 | 2025-10-24 04:19:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff6fa937-a7c5-32ef-a658-c734e244eb3d | -6.43234 | -45.66845 | 2025-10-24 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0bf87b4e-6e79-3798-93b8-c09f71a3db08 | -20.48941 | -44.37233 | 2025-10-24 04:19:00 | NPP-375D | PIRACEMA | MINAS GERAIS | Brasil | 3150604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 03364c41-ce96-36aa-8063-e30f981c6242 | -8.41431 | -45.66526 | 2025-10-24 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96b543bc-f961-3f3a-af50-251824b27e4a | -12.80936 | -48.65944 | 2025-10-24 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f789133b-b5e6-34e5-873c-29294c21ea30 | -12.82565 | -48.6322 | 2025-10-24 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 476ffc65-51f4-3166-b44b-536a7e4eb773 | -6.78263 | -45.49244 | 2025-10-24 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ade1b2d-50a6-3bde-b9e3-4ea0b1a8369a | -7.02223 | -41.80626 | 2025-10-24 04:19:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5cfb219d-8ce1-3869-84de-1ae5e7373bcc | -12.3684 | -51.47287 | 2025-10-24 04:19:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6437b0c7-4c53-3bd2-8e25-8077b4cffd5a | -12.82843 | -48.63426 | 2025-10-24 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 408c98de-e118-32cf-89cd-7b100b311b55 | -14.92308 | -48.13802 | 2025-10-24 04:19:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51c8a296-23fc-363a-a994-ef7e6657ed66 | -14.54059 | -48.03273 | 2025-10-24 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18af6674-6e47-3f7e-ab76-ae7606e3f7e9 | -6.78103 | -45.48037 | 2025-10-24 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 53cf9165-5d24-3b7b-81c9-0b8b0efa0fe3 | -6.10904 | -48.10312 | 2025-10-24 04:19:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2254000e-a1c4-30b2-94e6-521ee6b958d7 | -13.26397 | -47.89354 | 2025-10-24 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7b9cdc4-6a4f-388c-b902-b7c98d1f1b2f | -18.3599 | -51.71054 | 2025-10-24 04:19:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97f8c5a9-6d7c-3029-8b62-e72065f6ac62 | -8.17075 | -47.75999 | 2025-10-24 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 398a69ca-1837-3fad-bda0-e48c3dc4d6c6 | -8.65057 | -44.78801 | 2025-10-24 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f0f3bd6-0613-3338-9f6e-655aa4b33596 | -8.57335 | -43.78603 | 2025-10-24 04:19:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 60a7fc2a-e5a7-31dd-a435-71fe7bdc8245 | -15.60374 | -45.91243 | 2025-10-24 04:19:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ed686fbe-0d9e-3689-aefe-9599ca92075d | -7.18665 | -43.86834 | 2025-10-24 04:19:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5c9ce77-57af-31bd-897a-da8bf9be01df | -7.63778 | -42.20245 | 2025-10-24 04:19:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b242a7dc-09a2-3b9b-839f-2996855f8d1a | -7.72767 | -44.79444 | 2025-10-24 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7cb0808-0bf5-35ca-93c3-01dae07cd23d | -6.97198 | -45.50699 | 2025-10-24 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1d7e427c-db79-3145-9708-c36b8b5c457c | -8.66122 | -44.78613 | 2025-10-24 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54e01e4a-9f2c-3ce0-b9b7-a57fd974ab4a | -15.84355 | -49.08812 | 2025-10-24 04:19:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d586343-1b24-3672-b42c-c2e0702bf2ea | -8.35248 | -46.17866 | 2025-10-24 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b60a68b-aaf3-3aca-ae15-21f0415cfdea | -6.77818 | -45.47598 | 2025-10-24 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 622f726d-f642-354f-ae6c-1649baf966e0 | -17.65095 | -46.67036 | 2025-10-24 04:19:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c021d89a-708a-350d-9f95-eed078787568 | -6.4282 | -45.67176 | 2025-10-24 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48afec23-94f9-3591-9df8-c3547ef69fff | -12.67342 | -48.63736 | 2025-10-24 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b02776c5-35e9-358e-8690-7b4b90e5a876 | -7.62627 | -41.84917 | 2025-10-24 04:19:00 | NPP-375D | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 95ea8a4c-3986-34d5-a4d3-46a34573b1ea | -8.34573 | -46.19798 | 2025-10-24 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9055df26-35cc-3388-9f85-285919bffaca | -14.77479 | -44.97601 | 2025-10-24 04:19:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa9b8335-6bd2-3432-953a-9e9b2da5b278 | -12.82238 | -50.96619 | 2025-10-24 04:19:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80e8d4c6-5e84-387f-84d0-4ec79bd279da | -17.43181 | -46.20496 | 2025-10-24 04:19:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| de94c4dd-9a5f-307e-bafa-9f23b5362dc3 | -7.97964 | -47.23853 | 2025-10-24 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 156f2b1d-fe30-3355-99f5-9bb41fdc0e4b | -6.77407 | -45.47927 | 2025-10-24 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 78200e2e-337d-3b7f-90e4-365f4c209d35 | -13.64222 | -49.46044 | 2025-10-24 04:19:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ebb69a8-270f-306f-8598-aabab9228f95 | -19.34644 | -49.92979 | 2025-10-24 04:19:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 22fb6856-40d3-3e2a-be9b-d56f5891adee | -7.64223 | -42.17381 | 2025-10-24 04:19:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 49cce77b-cddb-3ef0-9d42-df4d28f1334d | -8.24144 | -47.17463 | 2025-10-24 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f090b3f7-491a-3c09-870f-42cdc08f861d | -9.6061 | -46.9099 | 2025-10-24 04:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| a95026f9-c36f-306e-a643-ed3118670293 | -20.92462 | -55.77763 | 2025-10-24 04:21:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README32.md)
