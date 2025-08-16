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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 495c53c3-dab9-3495-af89-35307944d4cc | -9.19177 | -59.68657 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac404b69-aa03-374c-b850-916b4e7a8c18 | -9.06376 | -58.94685 | 2025-08-16 05:23:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c956dd7e-4065-33fa-83be-225ed81442aa | -3.23584 | -50.807 | 2025-08-16 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 05098cfb-dc1f-391e-b3ea-9e322e9e7340 | -6.92615 | -59.64397 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd97e1a2-2bb8-3ccc-a3e3-28773128b7fb | -9.00059 | -60.49791 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6b55db3d-974c-32ef-9f7f-082d9535ee65 | -7.06222 | -59.23732 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0af4648e-4cd9-37b6-b352-5c2d9d0d7aaf | -9.50087 | -60.55825 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7419a578-5b33-37ff-8186-bc7c996c01a0 | -8.94167 | -62.22111 | 2025-08-16 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77fd9b80-642d-3760-9d66-11ff891ce16b | -7.04224 | -59.61804 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b265b0f-2b45-39e8-89c7-d5049078cd53 | -7.61367 | -63.33566 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f16771bc-f746-34f9-ad7b-55b0ce2617d8 | -8.90733 | -60.72763 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 714ef32c-177d-3aaa-9f6a-942a740e86e9 | -9.50459 | -60.51178 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a9c4420-0106-3d4b-9c60-974fa25fb4bd | -10.38973 | -53.46627 | 2025-08-16 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 81f4ecf9-e65f-3da3-bb0b-462ed1c1c932 | -3.38045 | -52.71748 | 2025-08-16 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1329fd2f-0db1-32ce-b839-31fb3a6280ea | -9.50916 | -60.54871 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4893abf3-abdd-37f0-9658-e24d0e5f987b | -7.0831 | -59.23684 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a17bf439-a5c8-3612-9c99-badbc07fc3d4 | -9.18151 | -59.66245 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25be778f-fcb8-3c97-9b36-8b573386bd58 | -7.61777 | -63.33237 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a596581e-9d03-3b94-a78f-74511f19a1d5 | -7.58646 | -61.41093 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed36ba4b-e65e-33a1-a0b8-3216af0db33a | -7.82006 | -61.33101 | 2025-08-16 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fcdfba57-8162-33a5-a55f-f93acd56efc1 | -9.20694 | -59.65501 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d261db8c-5563-37ef-ae7d-87b058a498f2 | -8.9885 | -60.53207 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 6b49bedb-56a7-3a3f-a74a-31cbc3a39c9e | -8.66513 | -63.84936 | 2025-08-16 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a17de83c-c73d-3f6d-84c1-799ef5923e20 | -8.98572 | -60.52803 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 5471766d-9d71-3d64-afd3-1e99c5b2084c | -7.49987 | -61.31194 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e5213f4a-c381-3e9e-915f-e2e8446a8420 | -4.22792 | -47.22082 | 2025-08-16 05:23:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a9f14cfd-adcd-388f-a194-1f4478015075 | -7.42329 | -60.03583 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9a41d94c-fb49-344f-8770-cd03f8d24ef7 | -7.28514 | -60.6214 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f517acd4-4764-34d7-bfe1-c3537069d138 | -7.60026 | -63.50452 | 2025-08-16 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c4ca32b-7422-38cc-8636-dd5f2aa266ab | -7.04504 | -59.62214 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e037dae-f017-302b-a120-707da50fce51 | -7.56219 | -61.41423 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a457e6e5-3d05-38c1-927a-ada1d2f0d046 | -8.46876 | -64.05241 | 2025-08-16 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da78dc4f-8feb-3585-a233-efc641cf82f8 | -7.0701 | -59.23108 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 966963eb-ad10-3297-a41a-4e6a1d6f1163 | -11.26161 | -50.46939 | 2025-08-16 05:23:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ff31f8a-2144-375a-863c-a37f966e4361 | -7.52737 | -61.37675 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8de93ae5-9382-3ad8-934e-7cde97645bc5 | -10.43381 | -60.27887 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1504a8f0-a8b5-30ef-b23a-454bbbf91475 | -8.80351 | -52.07026 | 2025-08-16 05:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 53be8800-a8a9-31cb-8626-ffde16dab4be | -7.61903 | -63.32469 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 237adfb2-a04b-3051-b8ab-f23c519a3226 | -9.3719 | -66.57493 | 2025-08-16 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb03db6e-3e3b-31a8-a88d-abba98961b7b | -7.56387 | -61.42516 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd9c1218-3027-3f4b-a63c-116b21a0d1cc | -7.95551 | -63.46096 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfb8a056-87a1-37dc-b17d-70df58b914ca | -9.17442 | -59.63483 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d857eb3-7e2c-3979-9c91-27b6358e6e0b | -8.98457 | -60.51344 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 99cd2841-bf61-3262-bf4f-c19dd87e2e78 | -7.52786 | -61.33056 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 96660569-09b4-3aef-a541-730d70f94e26 | -8.9862 | -60.50287 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| cb1b1503-b3d4-345f-a226-55ec472498e7 | -8.66574 | -62.45722 | 2025-08-16 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 290c98d0-966c-3aaf-94f7-337158a0cad5 | -9.1716 | -59.65325 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0706bd55-1885-37b1-a60a-a31a0148a653 | -7.63007 | -63.32253 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de15cefe-56f9-38f8-af73-2d3efa691e89 | -7.87922 | -61.81953 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5a8dcab-ccfa-3ae7-bc1a-a24b4c0aac56 | -8.99454 | -60.515 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b9acfad-8502-3b05-a967-d8bfc9bd7b85 | -8.96548 | -61.6822 | 2025-08-16 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9f929432-8645-3674-8b3d-d48d523061ce | -8.90234 | -60.58347 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 995e1ca3-7215-3da3-aa12-d4b7d4992571 | -7.07916 | -59.23994 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 140e5bcb-4f79-379a-8885-c6720cf05c77 | -8.99291 | -60.52557 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 46548f5c-6fbc-3251-9087-82428316917f | -9.15409 | -59.67689 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 745b75c2-3c42-31ea-95e5-5abe5c3398da | -7.95728 | -61.75652 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e41d10a-e23c-3095-9112-0d903cba35b3 | -7.92298 | -61.73673 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 729cdcef-2de1-3a55-9958-922770ca8480 | -7.8759 | -61.819 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a98e127-cbb0-342c-8f43-5bc4642384ba | -8.98233 | -60.50587 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| e1a0b04e-2477-3a33-adbd-350ccecebf41 | -7.30884 | -60.62155 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f51fdf2-c15c-3919-bdb3-d55d4faba4b5 | -6.94144 | -59.54421 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 788adddd-2e35-31df-a8aa-b62c42935ef9 | -8.98417 | -60.56019 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ad366e0d-108c-3c07-a1dd-9bf7aaba0f4a | -10.07071 | -59.66678 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ddc69d01-0b4f-391a-b3b6-ff70b33ad84e | -9.81148 | -48.53848 | 2025-08-16 05:23:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c0a5c3f8-d1c8-363f-898d-9d337103b471 | -8.99074 | -60.53963 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f654756e-65a6-3f0a-a69c-d22ad6cdc0c9 | -7.92242 | -61.74023 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ac2c6dd7-9933-3ae6-aa5a-cfae31b83f59 | -9.38806 | -60.54081 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc139010-3909-3134-9253-9adf187174c7 | -10.50585 | -53.59212 | 2025-08-16 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8473d2b7-25bc-3fa9-824e-aa08fe801e53 | -3.49161 | -51.1922 | 2025-08-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b6e73e2-bf35-3898-bbc1-dd8b57b5914c | -8.98348 | -60.52048 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fd146bdd-a2e3-3558-b2c2-aa5bcf698bc7 | -8.97906 | -61.70575 | 2025-08-16 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 44.5 |
| bfbef07c-ef13-3135-bd04-e1574b833c50 | -9.01754 | -61.22004 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ddd69737-2143-3a24-bb93-c36ae5a9b646 | -9.79285 | -61.50428 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d858640-7486-3f24-8a81-c6aa2abd6328 | -7.91934 | -70.22715 | 2025-08-16 05:23:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1bdabd08-2f72-35d6-b4f4-6b95568d6a2e | -7.30222 | -60.62052 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa5e5b3b-a442-3a54-a6be-de2be5eb7c05 | -7.67481 | -63.31004 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e8d90ca9-aaea-3dca-ae15-0120f3fee4db | -9.34661 | -62.58545 | 2025-08-16 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1b72d60-b20e-3cbc-970b-7966190d29c2 | -9.21429 | -59.65237 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 877850f2-0bab-3587-ae51-ffd8cdaedf43 | -6.94527 | -59.51915 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e3d66b28-fb6b-31f9-8e76-e20cbba602fb | -8.93553 | -62.23824 | 2025-08-16 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78876275-a788-3104-a1db-1e451c58d6b3 | -8.99135 | -60.55772 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4dd1a226-4f33-3a9e-8ce4-6f38bd750677 | -9.16651 | -59.66379 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c38e06a-e83d-396a-ba54-dd3b34e0d2da | -7.32646 | -60.6172 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f5cac809-3ab6-315c-a08c-68a387ae970a | -7.42662 | -60.03634 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d8b94952-da22-3b09-82bb-b1a2ceb6fde7 | -13.02835 | -56.87045 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b058994e-91a0-3624-8c4d-a9eedfbec06f | -7.5368 | -50.5308 | 2025-08-16 05:25:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72c57984-24ac-349e-b325-fbf787f004bc | -11.3535 | -55.42099 | 2025-08-16 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| daf70dff-9611-3bcf-bfb4-4d08b6134291 | -6.14265 | -57.93081 | 2025-08-16 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5c6248f3-c916-31a1-811b-9633fcdc158a | -14.93555 | -54.70749 | 2025-08-16 05:25:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 7dcf68d9-1180-357a-86d0-8c8bf48773d7 | -9.55996 | -68.58024 | 2025-08-16 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c60fdd24-0a5d-388b-a0cd-fa493e93abb9 | -14.87114 | -60.08282 | 2025-08-16 05:25:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 73475e87-8a43-3664-87e2-7ff26bbf2091 | -10.33014 | -64.47515 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7f20484-ec5b-3218-bfb6-730027a8c9fe | -11.35733 | -55.42591 | 2025-08-16 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07e402f3-3cd2-3529-b219-d28c008f8da0 | -6.6705 | -58.81345 | 2025-08-16 05:25:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c908122d-552f-3d32-af22-f382d27e0df3 | -10.47111 | -61.31957 | 2025-08-16 05:25:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e412f15-1d20-3a9d-a628-7d4547a2a40b | -14.96042 | -54.73449 | 2025-08-16 05:25:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| f8a8cca9-ff5a-3abc-84d7-6dd805b9bee9 | -12.67035 | -60.25238 | 2025-08-16 05:25:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4b44559-74dd-3b61-83d3-949250fd7ec1 | -5.93144 | -53.65125 | 2025-08-16 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c8e913a3-afdb-3911-ad94-a8c299f6c740 | -8.79284 | -71.02651 | 2025-08-16 05:25:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41738481-ba5d-3fb7-845d-0ced10ca38f9 | -11.73025 | -64.89726 | 2025-08-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README60.md)
