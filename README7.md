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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74fb63e6-fd68-3d6e-972c-c72aa7efb224 | -11.68535 | -44.84752 | 2025-05-15 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ee6bad5b-7016-3b69-8b98-e2522f1b0ee6 | -17.80172 | -44.35975 | 2025-05-15 04:27:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5ad35b0d-b336-3dd5-83a0-3ffd429adc1f | -13.27932 | -45.42186 | 2025-05-15 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e7a2dfd-c7d6-36ee-9a7b-f34235071a98 | -12.72647 | -54.97329 | 2025-05-15 04:27:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6874088f-6bf8-39f3-baaf-29a1833d7609 | -15.38989 | -48.00879 | 2025-05-15 04:27:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 29ae5716-8814-305c-b765-66369161cc11 | -10.34276 | -47.97395 | 2025-05-15 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3aa98843-ccd6-32e8-9b2b-2d0a8d5ade86 | -13.28976 | -45.44752 | 2025-05-15 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3df043bb-f475-304e-a1e3-f9f7e5c0396f | -11.77758 | -47.35527 | 2025-05-15 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ccff7bd-a414-3e67-9d0f-a1800040c517 | -11.65236 | -58.26569 | 2025-05-15 04:27:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dfdadcbe-069c-34cb-b0b3-26c5a00aba17 | -12.68663 | -58.13522 | 2025-05-15 04:27:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a9981fc-af00-3dc9-8573-e6b51290a051 | -10.35273 | -47.97554 | 2025-05-15 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d6897304-ab97-3a4e-9ff2-bd13cf34d6ed | -12.35025 | -49.95702 | 2025-05-15 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ffa5d6a-b449-3972-ae91-05635425e3ff | -13.07983 | -47.81458 | 2025-05-15 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31dadb11-36ac-3a56-8975-d36b03858221 | -13.59632 | -47.38183 | 2025-05-15 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2dbfb5e-59a3-31cc-89e4-0a638c6d20bf | -10.33282 | -47.97186 | 2025-05-15 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d5668b0a-6f59-3cb0-8c66-bfea453fb5f4 | -13.6663 | -53.9339 | 2025-05-15 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b7cf8cf0-7d9e-3901-b8b6-4d685edcb9a7 | -11.6819 | -44.87145 | 2025-05-15 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 468d4d6a-7062-3f09-b9b2-b734a08eb39b | -13.28107 | -45.43417 | 2025-05-15 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 59138a4e-9e69-33a6-a1a1-7e2fcaa1ac5a | -12.19857 | -55.21737 | 2025-05-15 04:27:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 920a9546-10ed-3621-88f6-7e80f4146d72 | -13.28455 | -45.43468 | 2025-05-15 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67b71879-d3d6-395b-a8ef-93e090e94c24 | -11.78803 | -47.35336 | 2025-05-15 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ccd154b9-8aae-3ad0-8ba5-0d06bc9df135 | -11.66056 | -54.94955 | 2025-05-15 04:27:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ad11fbb-a4f8-35f9-8b40-65848e2703e4 | -12.49439 | -54.39989 | 2025-05-15 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ada029a-b2fe-3d46-bc80-16815cd56972 | -12.35089 | -49.95312 | 2025-05-15 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa3c1237-fe7f-3e86-a33a-b9e1d42e08e7 | -14.00718 | -53.00866 | 2025-05-15 04:27:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45001a70-ec6b-3627-9a51-19188f5e343a | -15.26632 | -51.46385 | 2025-05-15 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 4410fe35-5353-3990-b032-c516c8d79bd0 | -13.67053 | -53.93476 | 2025-05-15 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ca17b796-bcfa-3ff8-841a-8975364a3829 | -11.60973 | -48.0106 | 2025-05-15 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c2b14578-2211-343a-9d13-dba1df709714 | -11.78142 | -47.3523 | 2025-05-15 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 53ab152c-65ad-36f2-9d89-48796073d6e7 | -12.08474 | -54.57707 | 2025-05-15 04:27:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee1774e0-b6ec-3f5a-bae4-416b30ca448b | -13.277 | -45.41346 | 2025-05-15 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 41799f36-c642-3f0f-9f43-973e9324ae0a | -11.56002 | -47.6139 | 2025-05-15 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| deb60ab8-da17-3886-a7b5-f419cf0f1262 | -12.7637 | -48.92868 | 2025-05-15 04:27:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| af0dfff7-82f2-3889-b252-98bf73b02232 | -10.3794 | -49.30713 | 2025-05-15 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 995606fa-8b2d-34de-aa2f-0e627dc9000b | -13.26833 | -45.42417 | 2025-05-15 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 385e9275-8593-3f32-822e-d220046b6315 | -10.47626 | -49.14486 | 2025-05-15 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cb9ec3d2-3e3c-3731-9d74-e55e8f69f5a5 | -10.34138 | -47.68133 | 2025-05-15 04:27:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bbc2e07c-48d1-361c-9de8-6aa1e5390d4f | -11.9696 | -48.12427 | 2025-05-15 04:27:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46655c19-ecef-3718-8b90-64e447b21c64 | -14.06659 | -57.11094 | 2025-05-15 04:27:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00a807be-7f0b-3a7b-aecf-92f78628824e | -13.09005 | -54.87088 | 2025-05-15 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9eea2797-5d95-3c7f-b457-1edd5e7f9db1 | -11.79696 | -49.32291 | 2025-05-15 04:27:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a48f1011-54ab-3ab8-a713-dfdae2605e9e | -12.68335 | -58.13377 | 2025-05-15 04:27:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 94afc46a-3eb2-322f-aa5c-b5e7096de45a | -11.84431 | -46.63704 | 2025-05-15 04:27:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72779f20-3bd8-3016-aa0d-1d936d517b28 | -14.06724 | -57.1077 | 2025-05-15 04:27:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02b188c9-bcec-36d8-9164-159bc2930556 | -14.64508 | -45.10334 | 2025-05-15 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0bcc4d60-7a4b-31de-b104-2bff6866119d | -17.11403 | -49.14039 | 2025-05-15 04:27:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c819504b-25a0-36f1-b03f-0871b164bc9b | -13.2689 | -45.42026 | 2025-05-15 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c4c80f6-37cf-3f6f-948c-ac4604fc7dfd | -11.59903 | -58.96012 | 2025-05-15 04:27:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bbd55a5f-8c1c-30ea-8c91-c817d5f6f602 | -15.76829 | -47.15688 | 2025-05-15 04:27:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9129200c-01a8-33fb-9852-5ead28469187 | -15.26346 | -51.45897 | 2025-05-15 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 529ba017-5e6d-3c76-bfa9-da31a681dc00 | -12.07372 | -45.73251 | 2025-05-15 04:27:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 10056480-5f5a-3207-9db5-38b4200f1b8f | -13.66701 | -53.92998 | 2025-05-15 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 65d8c0d4-e761-3f7e-a278-4ab55577b76d | -11.16678 | -48.67606 | 2025-05-15 04:27:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 492daf97-d46e-33b9-bf8b-bbcd2e0b3f45 | -11.00977 | -50.75959 | 2025-05-15 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 10113c46-2c3c-374a-ba84-64eb04398340 | -11.78418 | -47.35633 | 2025-05-15 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 11052e54-ff0f-3be6-9bdf-3815d4072901 | -15.40473 | -48.41605 | 2025-05-15 04:27:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a76e3791-2c52-3cc8-aacb-704a0c026eaf | -15.56982 | -47.85529 | 2025-05-15 04:27:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ec8a49d-618d-3b11-a488-ee0808ef9ca2 | -11.38704 | -52.93937 | 2025-05-15 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6c97e380-fea6-3a8d-a211-7e1128e90b61 | -11.79078 | -47.35739 | 2025-05-15 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd336db9-789e-3508-aed9-a747ac4a0f2a | -11.24226 | -49.49102 | 2025-05-15 04:27:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f1e4517-79b1-3881-8b5e-813372031b9d | -12.12016 | -54.66703 | 2025-05-15 04:27:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf3d7037-276a-3adb-8b03-a26ac82f67eb | -11.58313 | -47.61762 | 2025-05-15 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a9bf779a-2b80-3fa3-96f9-4c9781d2fc53 | -13.27817 | -45.42971 | 2025-05-15 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ac31e9e8-640a-30b9-8a2d-9b5133466898 | -12.10214 | -49.3075 | 2025-05-15 04:27:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 92f987f3-b7bf-3855-9d07-508811ed6038 | -11.78527 | -47.34933 | 2025-05-15 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c1a31d3-0e01-3052-900e-11f9eaee3926 | -14.45174 | -51.54367 | 2025-05-15 04:27:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15e9e957-75bb-332f-bedb-1a1da2ae7c3f | -13.07119 | -52.02005 | 2025-05-15 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fcab70c-3921-36f9-89dc-e75cacdb267e | -11.57036 | -47.43987 | 2025-05-15 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ccde5631-f806-37ae-8b40-d1c1821964eb | -13.27875 | -45.42579 | 2025-05-15 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0068ae7b-15b6-31f9-bc37-74030a729bcd | -21.05571 | -55.99501 | 2025-05-15 04:29:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3b47772-167f-3f2b-8152-605910a9e243 | -22.3245 | -48.81357 | 2025-05-15 04:29:00 | NOAA-21 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 587ab7b4-2a41-360f-a41a-197871362e23 | -21.78073 | -55.31748 | 2025-05-15 04:29:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3db35dcf-b1b4-3f46-ba4f-b9ed7fab3f02 | -19.05284 | -53.45671 | 2025-05-15 04:29:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd18a05f-907c-39c6-9d17-392e0484d934 | -23.40566 | -46.5586 | 2025-05-15 04:29:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 247d9335-866b-38a5-a2d9-6502d08240b2 | -22.26102 | -50.35563 | 2025-05-15 04:29:00 | NOAA-21 | LUTÉCIA | SÃO PAULO | Brasil | 3527900 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| c112dc4d-33ef-33c2-9fe0-176595b0a588 | -19.88592 | -44.07026 | 2025-05-15 04:29:00 | NOAA-21 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a07a27be-6fdc-3822-94b8-224b303bebb6 | -23.60781 | -48.29504 | 2025-05-15 04:29:00 | NOAA-21 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 45.7 |
| dcdcba6d-0e7a-3b0f-b1b5-4152c59a9532 | -20.23098 | -46.75329 | 2025-05-15 04:29:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44452e95-388d-35d8-a5f6-67670b2d536c | -21.05428 | -55.99783 | 2025-05-15 04:29:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38ebdf91-e93a-31be-be41-94d1b4932e91 | -19.06503 | -53.454 | 2025-05-15 04:29:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fe962ea8-92ed-3739-a199-53b0373a313c | -20.5063 | -54.73348 | 2025-05-15 04:29:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 93f73efe-89bb-3d54-9a1a-071f8f5c2bde | -20.98214 | -48.48312 | 2025-05-15 04:29:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f258fd92-925a-39f7-a509-12e454c8f8aa | -19.87574 | -47.36063 | 2025-05-15 04:29:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b83ab9d-0442-3a8d-956f-b18c41bc908b | -20.20937 | -46.75378 | 2025-05-15 04:29:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0c2e190-8a7f-37bd-a9bc-1ba14f04c8ae | -23.34019 | -46.77385 | 2025-05-15 04:29:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1b187b48-f97b-3bd6-b5fa-ca9fb18f2116 | -19.15961 | -47.82153 | 2025-05-15 04:29:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3cad389d-0f74-3c1a-8322-535704a9b1f3 | -19.16016 | -47.81781 | 2025-05-15 04:29:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 26702a77-b282-3840-99fc-f6ef91028b82 | -21.17538 | -56.48608 | 2025-05-15 04:29:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cb194b85-63bd-3eef-9a6c-a1e71da544ec | -20.52071 | -47.35395 | 2025-05-15 04:29:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16c14f32-badc-32e7-b2de-149bf6a071fc | -21.05492 | -55.99914 | 2025-05-15 04:29:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ead0a4bf-32b7-3b0f-a6ae-3f61fe1f70dd | -19.06127 | -53.45324 | 2025-05-15 04:29:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2e042439-2fa8-355d-8245-08efa337b18f | -20.59562 | -47.87728 | 2025-05-15 04:29:00 | NOAA-21 | SÃO JOAQUIM DA BARRA | SÃO PAULO | Brasil | 3549409 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c8ffb6f6-d91d-3d85-a3ca-aaecfdb3d782 | -17.88078 | -51.1918 | 2025-05-15 04:29:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c4f90135-09c1-3884-a1be-c50fb7a15780 | -19.18706 | -47.20973 | 2025-05-15 04:29:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6057f5f5-a020-3ca6-bf2a-7466022bdb96 | -22.32507 | -48.80977 | 2025-05-15 04:29:00 | NOAA-21 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83d3d4a4-e002-32f4-9065-9f5f18846e1e | -19.98073 | -47.19044 | 2025-05-15 04:29:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6baaefdf-9337-38bc-940e-801b092a5e77 | -19.17528 | -57.54322 | 2025-05-15 04:29:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 2d3fa18d-ba61-32b1-a53b-b096f1ee1f1e | -19.05661 | -53.45743 | 2025-05-15 04:29:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98f96440-d88b-35b1-b495-29f2f87af9d0 | -22.14318 | -45.96932 | 2025-05-15 04:29:00 | NOAA-21 | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2140e89f-7088-3ab0-b065-37defd1e6db9 | -19.36855 | -47.62133 | 2025-05-15 04:29:00 | NOAA-21 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README8.md)
