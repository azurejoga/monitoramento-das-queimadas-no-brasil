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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c97fc54f-4d5b-3a26-9a37-8cc0d50d5814 | -13.3455 | -54.39194 | 2025-08-25 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba5b7ef3-7f30-389a-9ded-6f08217e0ab0 | -12.07212 | -63.14727 | 2025-08-25 05:06:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f76ce2c8-cce8-38e8-b056-08fe01129ff2 | -15.17897 | -48.20367 | 2025-08-25 05:06:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| deaf9da6-ae8a-3446-a61b-af2953878f20 | -14.28928 | -58.61034 | 2025-08-25 05:06:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9a1536b7-185e-35ce-a4d1-71e92a54e162 | -14.2826 | -60.3702 | 2025-08-25 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5246d26-468d-393e-a3e5-03478fa5c4cc | -15.08078 | -48.66521 | 2025-08-25 05:06:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 6f7964de-d35b-34d2-bf44-7b85b803dc90 | -13.61469 | -48.17918 | 2025-08-25 05:06:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc08eaa4-119c-34d6-90bb-8bc5fee83580 | -14.27838 | -60.37376 | 2025-08-25 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14da0aca-8949-3a84-b302-2ad4754121ad | -14.26165 | -58.61669 | 2025-08-25 05:06:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bab7946c-c3fc-3302-b65b-d025891e4f7a | -13.49342 | -46.88784 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d736be15-dd91-38ea-ac95-570e32bc43c5 | -17.34244 | -47.85601 | 2025-08-25 05:06:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab726e5b-ff7c-3db2-af69-aa261d065ef0 | -14.37358 | -51.93408 | 2025-08-25 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f10d35b-e459-3992-986d-84206119b5ed | -13.00404 | -56.88616 | 2025-08-25 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c6a13ede-ae9b-3ddf-88a1-f2674534d422 | -14.26223 | -58.61308 | 2025-08-25 05:06:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4bc8389c-97bf-3806-80e8-4ce326ca8f10 | -12.48398 | -53.8232 | 2025-08-25 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cfbcb201-6e89-37fd-aded-40c5d39e20f8 | -14.26389 | -48.04148 | 2025-08-25 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a2818dfa-df25-3306-8fc0-ac337c937886 | -13.40785 | -51.78461 | 2025-08-25 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2840580a-4fe3-332e-a4dc-fe0ee3b2b4c0 | -11.6315 | -61.20586 | 2025-08-25 05:06:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2a73932-0ba4-3384-911d-242713a1610c | -14.74037 | -55.93084 | 2025-08-25 05:06:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 96519cfa-307a-301f-894c-a8a83d0ad19c | -14.33991 | -51.96194 | 2025-08-25 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 36c57519-5dc1-30fa-998e-51520d958b3e | -18.38723 | -46.84104 | 2025-08-25 05:06:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 235cbbca-36f9-30b8-8a85-2349df1abf4f | -14.24047 | -58.62051 | 2025-08-25 05:06:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a99deb11-8e7e-38af-8908-12c9f0094b8f | -13.39522 | -51.8149 | 2025-08-25 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a5ddaa89-3318-35da-83c6-5d92fe11c1ef | -13.09389 | -57.20127 | 2025-08-25 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 91c581bc-17c3-3868-968a-6ef213877872 | -14.09664 | -53.99615 | 2025-08-25 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 77e0f518-f200-3034-be53-49b218c17724 | -13.45896 | -46.8798 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b709f4c0-57a5-3b9c-96c3-7677503a6865 | -13.49824 | -46.89701 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 44ac7c49-1c81-3ec7-bc37-3c3d0e5f3723 | -14.11119 | -53.99215 | 2025-08-25 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d231708-1def-3afd-aef3-fa205062ce57 | -13.4678 | -47.00597 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea22f95f-65ed-3a27-bd00-00ddbb391f4f | -14.10687 | -53.99609 | 2025-08-25 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 397789a4-5fe8-34c2-b675-84555f8f3115 | -12.15259 | -60.74398 | 2025-08-25 05:06:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 618598a1-053e-3483-bf97-ca090848eda1 | -13.67232 | -47.9717 | 2025-08-25 05:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24ee8024-8ce0-33f8-bc36-6534dfdf493c | -13.40731 | -51.78862 | 2025-08-25 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57405144-b97f-35d2-8569-3ff18abddd8a | -13.41258 | -51.78124 | 2025-08-25 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bbbc3e13-ebc4-3470-88fe-f3f2c06ed1db | -12.06217 | -63.15379 | 2025-08-25 05:06:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 943f93ba-e27a-37df-84aa-173770ccaad6 | -15.11445 | -48.64336 | 2025-08-25 05:06:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ec1e022f-ccd1-3d3c-ab82-a2af4442ed75 | -14.23322 | -58.62299 | 2025-08-25 05:06:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4be6cb11-61d4-36ce-8323-be383a51e951 | -12.99298 | -56.89164 | 2025-08-25 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0e88aea8-ba0d-31e6-a668-baf950e29770 | -12.49065 | -53.82867 | 2025-08-25 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| caad3996-6493-3be4-8585-af7d0e47db42 | -14.42585 | -56.46422 | 2025-08-25 05:06:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1358d24f-9912-3b02-9e53-81169394e165 | -13.45312 | -46.87929 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52191d00-75b1-3031-a65f-4e27f8319b46 | -15.76353 | -49.97046 | 2025-08-25 05:06:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aa49ae4a-e4fa-3c29-92c4-ca3252702a0d | -14.43257 | -56.46527 | 2025-08-25 05:06:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5520681c-d998-3864-9cd6-422c999474db | -11.69246 | -60.18035 | 2025-08-25 05:06:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b4b78f1-a6be-320e-a0c3-475bb56003a9 | -14.25841 | -48.04109 | 2025-08-25 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 42c446f9-0e0e-3afe-ad74-e22bd66d914e | -14.10466 | -53.99283 | 2025-08-25 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6d1dc179-7cd5-31b2-a349-8e2510a227a3 | -14.37725 | -51.9386 | 2025-08-25 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae5e12e9-4de1-3fdb-90db-18ce20256c62 | -14.51036 | -51.911 | 2025-08-25 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 8aa93890-03f1-3474-b39a-29f8e2052281 | -13.4929 | -46.89221 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a371a19-68f6-3e7b-ad97-afe2b48df077 | -13.46194 | -47.00607 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e5510921-6da5-3752-b617-0d6946785dca | -14.09729 | -53.99166 | 2025-08-25 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 41cafe1d-1b7a-3442-963c-7faf5f438d81 | -14.38457 | -51.94765 | 2025-08-25 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb1c7d3e-4e2b-3a07-923e-4008fdb39f5e | -15.15296 | -59.58884 | 2025-08-25 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45d3116c-f198-3280-bf97-736000ecde83 | -14.30316 | -60.37712 | 2025-08-25 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a233ccc-ce8b-3d37-8ed2-43d5a903b595 | -18.2977 | -49.53449 | 2025-08-25 05:06:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 26101ed9-eaf9-3c0a-b612-008079b1be4e | -15.07633 | -48.65743 | 2025-08-25 05:06:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ba4cec9-9ed5-341f-8940-5c5dd8663da1 | -18.23255 | -49.26155 | 2025-08-25 05:06:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ecb0dda-b3c2-3afa-a0df-1e8e90825625 | -14.29676 | -60.37212 | 2025-08-25 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11ccdfbe-e829-3b83-b448-9a6700443d54 | -15.62774 | -52.70592 | 2025-08-25 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df168f1a-3b0a-3fe2-b677-65eb89c3a4a5 | -17.5796 | -45.38726 | 2025-08-25 05:06:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ab4c890f-27a4-3f86-b9c9-b165efc7ce97 | -13.43036 | -47.02628 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cf100d11-3129-30f5-84a2-85ce49496daf | -15.1104 | -48.67941 | 2025-08-25 05:06:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7b7688d1-4040-3cdb-8bde-7db4d4ac5406 | -14.50984 | -51.915 | 2025-08-25 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| de09dd40-0982-3f96-8283-2d2036cdf1f2 | -13.43069 | -47.02341 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1638c23f-5aa5-3745-bc58-bc47360bbc45 | -14.22655 | -58.62185 | 2025-08-25 05:06:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b49ad874-6e8a-3a5b-aeb6-c7169e391564 | -14.3222 | -58.59743 | 2025-08-25 05:06:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06524a48-f7eb-350d-860a-53244826c090 | -13.28466 | -47.51322 | 2025-08-25 05:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3bbf0b72-3e73-36f6-8b7b-3b29831d66a6 | -13.39211 | -51.80642 | 2025-08-25 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eba84c49-3a19-39f2-979c-bab47ad75196 | -15.08162 | -48.65812 | 2025-08-25 05:06:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 9d26b0e3-a290-329c-b56f-3e6c440a12e0 | -13.4624 | -47.00209 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 47734b3a-2304-3fc9-80c3-98743c42a675 | -15.15172 | -59.59638 | 2025-08-25 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0c66ec0-d805-3182-a6a1-363a6eee5252 | -13.61426 | -48.18282 | 2025-08-25 05:06:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c548c040-6197-361f-aa10-c80a50dc1a76 | -15.17461 | -48.20237 | 2025-08-25 05:06:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b0c6fe2d-6d6d-3d83-9281-84a4cd2fab5b | -14.64787 | -56.56688 | 2025-08-25 05:06:00 | NOAA-20 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 618e4a8b-bff6-3c6a-9600-f332a46a7c22 | -14.28328 | -60.36619 | 2025-08-25 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e51645c-dbd4-3000-a8f1-f98324a4756d | -13.68904 | -57.7556 | 2025-08-25 05:06:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce24101e-ef5c-358b-8d43-d7345a63aeec | -13.08726 | -57.20018 | 2025-08-25 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f131d2b3-5d71-3502-af44-d8139ef7b08a | -11.99279 | -61.02326 | 2025-08-25 05:06:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4db25e6-72bc-3aee-8fe9-115f3ee87b07 | -14.70311 | -54.68203 | 2025-08-25 05:06:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d45435a-7bf0-33ef-9b44-628a13ee8934 | -14.12163 | -53.99831 | 2025-08-25 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c905a7f3-650a-3610-899c-70d86218d1ea | -13.43022 | -46.92504 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f754135-fba3-31cd-85e5-84728a1bac14 | -13.43133 | -46.9153 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d61bd9b6-6ee1-3672-9c07-f2ecee1ea75f | -10.32259 | -67.36351 | 2025-08-25 05:06:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 57cf88b7-4432-3d34-836c-24d9db558902 | -13.50798 | -46.9143 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8775e2b5-5993-3c8e-a0b2-a4714f2f0fa7 | -13.43174 | -46.9117 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 99477474-fee0-3bf9-a10e-2b44902d08a0 | -14.64901 | -56.5819 | 2025-08-25 05:06:00 | NOAA-20 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0ff960e6-3d4d-35e1-8dc7-9975a357183b | -13.66688 | -47.97105 | 2025-08-25 05:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2c7a4e6-9e85-3524-b1a5-0a5a65834bad | -14.28681 | -60.36671 | 2025-08-25 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e200c9d-6fb7-3d6b-893b-d80ecc9a4627 | -13.66645 | -47.97468 | 2025-08-25 05:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9eb61906-654a-33c1-a233-22d7f0fbb2e0 | -17.57592 | -45.38934 | 2025-08-25 05:06:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 901bf7ef-c998-31a8-93e2-e10bb0e88652 | -13.61595 | -48.16856 | 2025-08-25 05:06:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9240f431-dc4a-34d0-b302-ab6169291196 | -15.1197 | -48.64446 | 2025-08-25 05:06:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 15fa9d88-8544-33f0-ad41-0f95014431bf | -14.30094 | -60.36878 | 2025-08-25 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f628b64-9478-30c1-bac9-7b5adbe1aa67 | -14.43817 | -56.47364 | 2025-08-25 05:06:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a2f8e70-17e2-3909-b147-dcb137c85ed0 | -15.10353 | -48.69922 | 2025-08-25 05:06:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33a9d84a-04a2-3441-96d4-3874e5649ec9 | -17.58002 | -48.48585 | 2025-08-25 05:06:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 55b5849a-80f6-3ad0-a344-a794f13f54cf | -14.38595 | -51.94326 | 2025-08-25 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 849d1f4b-e076-3fec-9ac9-0dd51590aa93 | -13.0068 | -56.89025 | 2025-08-25 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cfef8cbb-6ffc-3a73-bba7-7cdc653f8b1a | -18.34241 | -46.02012 | 2025-08-25 05:06:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| eba863e6-290c-30b4-91ee-e3d29634f77b | -14.64846 | -56.58552 | 2025-08-25 05:06:00 | NOAA-20 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README74.md)
