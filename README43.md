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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac152e05-4336-370d-8700-1c52991b549c | -14.90745 | -47.75682 | 2026-09-12 05:12:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7868feb4-02d5-33fd-8ff3-d167110c3db5 | -12.59508 | -53.98565 | 2026-09-12 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8963097d-3942-3b1e-974e-9f420dbacf5f | -9.90686 | -67.82571 | 2026-09-12 05:12:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28759783-9b89-354f-9145-552a8981843c | -12.13561 | -48.95744 | 2026-09-12 05:12:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 246632f1-d09b-3a78-9094-0818f22091a1 | -9.18915 | -68.21217 | 2026-09-12 05:12:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d5d52c14-054d-3752-8d50-be44528b6a9e | -15.0211 | -48.50195 | 2026-09-12 05:12:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cfab5d1b-e876-30cf-8a48-58d5eb9dea94 | -15.25055 | -53.89289 | 2026-09-12 05:12:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 234883fd-575f-3d46-a653-4430b515463a | -12.15321 | -64.14326 | 2026-09-12 05:12:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 92069418-1768-32c2-97a6-717f1d9e2faf | -17.10758 | -51.25698 | 2026-09-12 05:12:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6e19fe38-ee2a-3449-9299-540084bf1ec5 | -13.36855 | -48.02187 | 2026-09-12 05:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7269a64f-894e-3623-95aa-dcfd90e77dc8 | -13.37946 | -48.01358 | 2026-09-12 05:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8ed555cc-0e52-30a3-80e2-ef46f386fcfe | -12.85187 | -44.38967 | 2026-09-12 05:12:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a52042ec-f144-385e-b564-24998a1e4d4d | -15.55596 | -54.23924 | 2026-09-12 05:12:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71b10eb1-2f93-3169-9bf9-f1cdb424a381 | -9.46995 | -67.09789 | 2026-09-12 05:12:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 932780c3-a4fd-34ef-9e45-6616194007e1 | -9.71139 | -64.96257 | 2026-09-12 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1bdb41e5-569b-384d-a04d-de69a1752bb5 | -15.98565 | -52.72014 | 2026-09-12 05:12:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8a16758e-9fb1-32f3-a1b1-cf2a9f3bab4e | -9.17865 | -68.22542 | 2026-09-12 05:12:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 781ef2d3-6081-32a7-a495-7797e4ddceac | -14.58796 | -52.66023 | 2026-09-12 05:12:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c9b1b9de-6da5-378d-a691-d0576cd0350f | -12.64667 | -47.09143 | 2026-09-12 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c9b4861d-0a12-38b6-a5dc-4f3fae1e1170 | -9.17995 | -68.21899 | 2026-09-12 05:12:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c0e3aea2-e15f-3d96-9df2-30f54ceef3e3 | -16.52545 | -50.83066 | 2026-09-12 05:12:00 | NPP-375D | IVOLÂNDIA | GOIÁS | Brasil | 5211602 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32baf0a6-224e-3042-899c-34da80e94359 | -12.11989 | -48.97256 | 2026-09-12 05:12:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b3a26f3-fa8e-3608-a9a5-eb5c32233d94 | -12.15495 | -64.13416 | 2026-09-12 05:12:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b616e4ec-4c88-3096-9639-936fce2c2b23 | -9.47165 | -67.09451 | 2026-09-12 05:12:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1e7f2fc-62eb-3b16-9aa0-51853e95e90d | -12.1538 | -64.14021 | 2026-09-12 05:12:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 667c21d0-9883-321a-9ed0-6e7fae235452 | -12.14873 | -64.13918 | 2026-09-12 05:12:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b1d5bc81-ac1d-30ed-8bfe-d19e5610bf09 | -13.37887 | -48.01835 | 2026-09-12 05:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 375d285f-36f1-3a43-972e-7e6cfcc1c229 | -10.28071 | -68.75469 | 2026-09-12 05:12:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5fa13950-ffa5-3e20-b9f4-0dcbcacd2c47 | -15.03913 | -49.44141 | 2026-09-12 05:12:00 | NPP-375D | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 525af38b-8717-3085-9601-7a6605c29ec0 | -12.1311 | -48.95699 | 2026-09-12 05:12:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1208a3f0-6a35-35f9-b2fa-857f30ee8357 | -11.24305 | -54.14249 | 2026-09-12 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3304d8d-1043-3d6b-bce7-c55bd85baa44 | -13.45951 | -48.49957 | 2026-09-12 05:12:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a7ce606c-49c7-3572-a024-71b6e3324733 | -9.44298 | -67.03198 | 2026-09-12 05:12:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c9a6922-43da-3115-9f65-21a64b50b91b | -12.12986 | -48.96623 | 2026-09-12 05:12:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 079088df-d5fd-3b16-9b35-bf6c4e05ef02 | -9.73587 | -64.95556 | 2026-09-12 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59cc3967-6fe4-33dc-b35d-0768fa9d63f5 | -9.45845 | -65.34721 | 2026-09-12 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 776e6042-5aeb-3220-b313-ee5113003db4 | -15.25501 | -53.89237 | 2026-09-12 05:12:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7bc7a48f-04cd-3941-a9cb-7d42b1910057 | -14.59061 | -48.83766 | 2026-09-12 05:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2e9b827a-8c15-3442-a13a-91e95531be10 | -10.5122 | -57.45612 | 2026-09-12 05:12:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ccb3d596-342a-3ef4-be6c-02ad798e6f00 | -17.03563 | -47.17456 | 2026-09-12 05:12:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3691f486-3e9c-30cb-8732-aa9e540a1931 | -12.85132 | -44.39431 | 2026-09-12 05:12:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1b71703-afc6-3345-bfca-62b5fcf74891 | -9.44402 | -67.02669 | 2026-09-12 05:12:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ebdbd06-b65e-36f5-979d-48ff4e350e67 | -12.63492 | -47.08843 | 2026-09-12 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ebc74b4e-a7be-3eaf-9fa9-f2f1b1d62fed | -9.45272 | -65.346 | 2026-09-12 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99a70be0-53bd-3820-8737-a5b9fd737a81 | -16.0325 | -47.90979 | 2026-09-12 05:12:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce2755e9-1159-3a7f-8359-d130f9702746 | -14.914 | -44.67134 | 2026-09-12 05:12:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dc65471b-ddc2-3f4d-b8bd-8bb5325b2125 | -15.51052 | -45.88792 | 2026-09-12 05:12:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9ca87230-7597-3400-b246-9406eca8f2a2 | -14.98209 | -53.95779 | 2026-09-12 05:12:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57a17131-9e55-304e-888c-38ecc11e38e5 | -9.19495 | -68.21531 | 2026-09-12 05:12:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8cfc32c2-360f-38cc-9e7b-c6aa0209e8e8 | -15.25464 | -53.88945 | 2026-09-12 05:12:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dd3b1191-63e6-33f9-9ecc-60249e934ddb | -12.12543 | -48.96521 | 2026-09-12 05:12:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e3428346-9db6-3887-b00a-0f4dd04c7ada | -13.30639 | -51.64266 | 2026-09-12 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 89cce9ef-b9f2-370a-a052-ae35a18a5701 | -12.64437 | -47.09595 | 2026-09-12 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f39a9255-eb62-3be3-9b88-bf593e7e39b7 | -12.64489 | -51.42375 | 2026-09-12 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f498e6e3-6daa-3d39-a302-ad9615117cbb | -11.24135 | -54.13111 | 2026-09-12 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04c80911-11b0-3928-bba3-42e4402d1d89 | -16.02707 | -52.66923 | 2026-09-12 05:12:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6ea08182-626a-32ad-929b-40558d075ec1 | -15.58787 | -54.52081 | 2026-09-12 05:12:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c3554a1-e845-3967-9cee-4f847724f743 | -14.83664 | -48.16869 | 2026-09-12 05:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b77a75ef-211b-357d-b5bf-4f53840f9845 | -16.0327 | -52.65636 | 2026-09-12 05:12:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d98410e9-da12-35ed-9c58-fc6d5537dd6c | -13.37788 | -48.00756 | 2026-09-12 05:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f0d9c5cc-472c-36f1-b674-b9e6c4218396 | -16.29248 | -53.84939 | 2026-09-12 05:12:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a17120d7-6153-3695-b92f-3159ff149335 | -13.37726 | -48.01234 | 2026-09-12 05:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b101a44c-50e2-3d2b-9051-0ccf7e6eaa2d | -14.58661 | -48.83165 | 2026-09-12 05:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7423a221-8d9d-36ca-b55d-6d8f4809fc9e | -9.18106 | -68.21718 | 2026-09-12 05:12:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1df886d2-16bf-3e1a-a07d-d8d5975b96a5 | -16.01136 | -52.69957 | 2026-09-12 05:12:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c3f9272-019e-3466-bb8e-2415690067ee | -16.02268 | -47.90565 | 2026-09-12 05:12:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 38116e56-2efa-3b9e-9776-cf1eb35d9a8c | -13.54052 | -49.48983 | 2026-09-12 05:12:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 120ad998-cf8e-3980-9fd0-f0ffc324c290 | -11.80585 | -60.45891 | 2026-09-12 05:12:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5a0ac5a-975b-3514-b97f-17af6849e8c5 | -12.13327 | -48.97479 | 2026-09-12 05:12:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 44e36c83-e7e2-3343-a8b0-8e8d42643383 | -13.793 | -48.80056 | 2026-09-12 05:12:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b149bef8-716c-379e-9665-ec0c0be53714 | -11.23457 | -54.10774 | 2026-09-12 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8abadefb-5c7b-3407-8fe7-0025b1b8ecc6 | -12.12317 | -48.98208 | 2026-09-12 05:12:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8132792c-6d75-38ea-9e71-3985311bd672 | -12.85117 | -44.39574 | 2026-09-12 05:12:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b3a09eae-ef7c-3e9a-9bcd-456cfdfcaf85 | -16.0278 | -47.90595 | 2026-09-12 05:12:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fcaa864c-c6e1-3a0f-8cb3-ee43e1422001 | -11.2425 | -54.1461 | 2026-09-12 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be3b8af0-f81e-36e7-976e-294649399da6 | -12.44341 | -49.58929 | 2026-09-12 05:12:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 801f5af8-27b8-39a3-bce0-d098a8e24d4d | -12.44397 | -49.58514 | 2026-09-12 05:12:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 59cef7a0-becb-3357-96e9-a49ba5889d16 | -12.858 | -44.39045 | 2026-09-12 05:12:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31d20605-6b13-35fd-a722-33231ffc2cc6 | -8.95314 | -67.38438 | 2026-09-12 05:12:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ff61ffb-78f3-3726-af26-20a85a8af7ee | -12.11659 | -48.96313 | 2026-09-12 05:12:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4a08913e-c703-3bd6-a158-2021f536ef73 | -16.96372 | -53.08436 | 2026-09-12 05:12:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5a06853-0100-3318-88f4-27f5f7f8857b | -15.61978 | -48.26728 | 2026-09-12 05:12:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1769196e-70ac-31e8-874a-c13fb5e0d051 | -9.47058 | -67.09988 | 2026-09-12 05:12:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 156800c3-469f-39dd-ab31-867a3e42a52b | -11.2419 | -54.12749 | 2026-09-12 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23c31a20-6c1f-3c1f-b244-009a895e0d80 | -12.13829 | -48.97137 | 2026-09-12 05:12:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2bac5efc-d096-3294-b5f4-51a660d1812a | -9.74142 | -64.95676 | 2026-09-12 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6683087b-0eb1-389a-a047-4dcca927bddc | -16.04019 | -52.65744 | 2026-09-12 05:12:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4604b9c3-19f9-38b0-803e-aa6d8ae3c14d | -10.5135 | -57.44834 | 2026-09-12 05:12:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 457851e3-3558-3912-9179-839de6c7ae31 | -12.1363 | -48.95228 | 2026-09-12 05:12:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5139538f-f426-3a55-9efe-cc67885b337e | -12.64477 | -47.09292 | 2026-09-12 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| abb4830e-28b9-3933-b51a-955b67dcb6e2 | -10.97033 | -54.10003 | 2026-09-12 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d465a558-e5ca-38fb-8539-177618b9c852 | -12.13884 | -48.96732 | 2026-09-12 05:12:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7e613aa4-6d06-3566-93a2-469efce51d8b | -12.20933 | -49.39918 | 2026-09-12 05:12:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11c5d8e9-18d2-3043-9a31-9c33114e0206 | -12.26939 | -48.57961 | 2026-09-12 05:12:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 85924cf0-6219-3773-a173-b9a18c4a30c5 | -9.18683 | -68.22025 | 2026-09-12 05:12:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 12f4af85-09c4-337d-a8e2-50fe87ca5bea | -12.64873 | -51.42432 | 2026-09-12 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 41b60c9d-8651-309d-a14c-b59133856eff | -15.55481 | -54.24702 | 2026-09-12 05:12:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd497d85-dfb2-3848-8975-a9cf47d08d56 | -9.34029 | -68.27347 | 2026-09-12 05:12:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 89530c57-b77a-30d1-b81b-cc98e0f24410 | -12.15885 | -64.14127 | 2026-09-12 05:12:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 777f769f-8fab-3d08-805f-1688588c0904 | -13.45829 | -48.50907 | 2026-09-12 05:12:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README44.md)
