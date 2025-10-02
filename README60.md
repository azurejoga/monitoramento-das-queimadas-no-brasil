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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03e65e42-85ad-387e-9857-2f7284f9640e | -5.14731 | -46.41397 | 2025-10-02 04:27:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd2390e5-50c7-3a64-b40e-c6565d40b168 | -6.08696 | -42.4997 | 2025-10-02 04:27:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3062073c-fd7f-3ee1-96ce-53dc163b946b | -5.71582 | -45.5107 | 2025-10-02 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01ecaca5-cc5e-334b-a1e9-4adabccf6776 | -5.75798 | -42.92858 | 2025-10-02 04:27:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 057d4f4d-b87f-33c8-b9f5-5df2cfda65e5 | -3.48814 | -48.9566 | 2025-10-02 04:27:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25ec8f7b-f34c-310b-b1bb-91aee70e7c9b | -5.80785 | -42.84519 | 2025-10-02 04:27:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 794027a8-5450-3580-8565-5b874b860ee5 | -2.70572 | -48.83382 | 2025-10-02 04:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ca54cf7-7758-33df-ae29-0c2c2b0bac2b | -5.69785 | -42.68563 | 2025-10-02 04:27:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 06d7a982-091c-3806-8ff9-d770e826d667 | -3.47382 | -50.02238 | 2025-10-02 04:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad77b87f-8ace-3385-9e81-e589c7c88bb1 | -5.64444 | -41.24423 | 2025-10-02 04:27:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 21c6acc9-9f1c-3f69-8a74-7183167decfb | -5.45892 | -42.84069 | 2025-10-02 04:27:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1416205b-0fc7-3374-97dd-28a021011904 | -5.42895 | -44.07712 | 2025-10-02 04:27:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 429ea860-a9dd-3dc1-922e-afbec500ef98 | -5.48866 | -42.76724 | 2025-10-02 04:27:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 39a19578-a4d4-315f-8d87-f2536c9bd07c | -6.09953 | -42.49257 | 2025-10-02 04:27:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4c75ddd2-01a2-33b3-a3a5-9e910c860ad3 | -4.46157 | -43.62061 | 2025-10-02 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fbb9235f-2665-3886-b187-49b8d7021e39 | -3.3472 | -43.18956 | 2025-10-02 04:27:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c778ca18-e888-3623-9912-1b823786c958 | -6.0492 | -42.6751 | 2025-10-02 04:27:00 | NPP-375D | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 42d30c80-bb94-3b34-ac5b-8ac7de762a47 | -3.09239 | -47.01556 | 2025-10-02 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90e34b58-b611-3d52-b314-2cf64ab319ed | -3.62652 | -42.77496 | 2025-10-02 04:27:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3c75a308-051b-31cd-875b-2f4a05ab9cb7 | -5.72305 | -45.50826 | 2025-10-02 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e9bc8459-768d-3160-b5d5-781fe2aa6c19 | -4.89289 | -49.9635 | 2025-10-02 04:27:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3ae438d-3fd0-35e4-a60b-c0a0fd0f78ea | -5.98112 | -44.58783 | 2025-10-02 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 373dc6bc-0cda-383e-aac9-0040740d93f7 | -5.83148 | -44.99024 | 2025-10-02 04:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd1b6a68-59b2-3e15-ac1f-3663a6c54d0e | -5.78629 | -45.75031 | 2025-10-02 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1c35a43-b979-3bb3-acea-25fded29eb16 | -3.34334 | -43.19185 | 2025-10-02 04:27:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1f486757-4d3b-39e4-a6b0-a3cefa4249e1 | -5.83822 | -42.79329 | 2025-10-02 04:27:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 54b7c3d3-d43c-3cdd-be67-3b2a73b5fee8 | -5.48584 | -42.73611 | 2025-10-02 04:27:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6a61f860-e1b6-340e-b43d-e8b6dcd7dee1 | -3.09015 | -47.00786 | 2025-10-02 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e83d3fe6-c53c-3475-8f6f-2317896a5adb | -5.99362 | -44.59723 | 2025-10-02 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d06d5905-0771-3897-bb35-f5a74fc00e31 | -5.63757 | -45.96547 | 2025-10-02 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a6697a8-eb81-3d76-8c74-9b203c98bcd3 | -3.87831 | -42.51604 | 2025-10-02 04:27:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b304e92e-a958-3582-887c-0e0a1c777c16 | -5.81516 | -42.84639 | 2025-10-02 04:27:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b12ed2d2-42e4-385a-89b9-7f8b7187ceea | -6.04556 | -42.44282 | 2025-10-02 04:27:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 46bce405-285c-3d15-802c-a31642d74148 | -5.98907 | -44.55899 | 2025-10-02 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b912340-7ead-3bb5-add6-427eaf487b24 | -3.45792 | -50.09472 | 2025-10-02 04:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 385faab6-09b5-3afd-a908-6df0115b7a0c | -5.70025 | -42.69479 | 2025-10-02 04:27:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 76758f5f-81ad-3eff-ba7e-1b852ce922ce | -2.92164 | -48.30312 | 2025-10-02 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f7641c4b-1311-37c6-a933-da331c957d0f | -5.98283 | -44.59934 | 2025-10-02 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| db4e805f-8371-385a-be24-9d359641196a | -2.26907 | -47.84996 | 2025-10-02 04:27:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2b38c33b-0b1d-38de-ae05-b68e228a6851 | -4.84679 | -40.79305 | 2025-10-02 04:27:00 | NPP-375D | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 251436a5-acda-3bba-b7e9-beda94060ce4 | -2.18366 | -47.08706 | 2025-10-02 04:27:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d56b04b8-8c37-3fba-b2ac-76cd6a13b895 | -5.24774 | -42.98231 | 2025-10-02 04:27:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 37dfa441-5062-3b21-92b3-7b2275c5b6f7 | -4.58445 | -45.61191 | 2025-10-02 04:27:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61ff8db9-1ae3-3109-b254-85ec99d1f31e | -5.8285 | -42.85727 | 2025-10-02 04:27:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 38ed61dc-9bef-3d33-a4b0-e9bf667c70bd | -5.69961 | -42.69907 | 2025-10-02 04:27:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 767eb716-2c49-347f-aaa6-0e2f73d631c0 | -6.05066 | -42.43425 | 2025-10-02 04:27:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fb8830b0-8a08-3aba-abca-8842a582ac2a | -5.17626 | -45.39097 | 2025-10-02 04:27:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b20fda51-3877-36fa-9365-c17ffa674dfa | -5.50245 | -42.72554 | 2025-10-02 04:27:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 20c0f842-ac4a-3b98-b3bd-e404a484c0b1 | -2.24532 | -47.88606 | 2025-10-02 04:27:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9624b07-7e05-3238-9295-bde7b852bd4c | -6.05407 | -42.43733 | 2025-10-02 04:27:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8eb01251-65cd-38e9-944c-04630ec25ce9 | -1.01742 | -48.95994 | 2025-10-02 04:27:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd18afb7-1da5-3e0c-8467-4700b06dedcf | -2.70275 | -48.82895 | 2025-10-02 04:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe4f1b41-eaa4-3e67-8d4b-d964e2f1355d | -4.31586 | -48.08916 | 2025-10-02 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 037345dc-c567-3d88-b504-86181f33922f | -5.24056 | -44.46113 | 2025-10-02 04:27:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d6ca26ab-4479-3208-9076-44ac3d1153fd | -6.1157 | -43.43512 | 2025-10-02 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e94d3b82-72c3-3392-a19e-875f2417d970 | -4.36841 | -43.01244 | 2025-10-02 04:27:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c997f567-6f38-3607-a181-7599b2f5556f | -5.98453 | -44.58836 | 2025-10-02 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1beeb904-2ed0-343a-9647-2ddccbafb8db | -5.98226 | -44.60299 | 2025-10-02 04:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c4fd348a-7d43-3557-bae8-0067529f3c49 | -3.87812 | -42.51425 | 2025-10-02 04:27:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c742e317-573e-3c2f-b96e-c384aa813e88 | -1.57833 | -47.31452 | 2025-10-02 04:27:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0dd94099-a1b2-3d45-b55d-bc933ffe756a | -5.48994 | -42.75872 | 2025-10-02 04:27:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1929945b-5433-370e-bb29-27bc2ccc9ae7 | -2.70641 | -48.82956 | 2025-10-02 04:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69fe1f51-7b1a-3496-ac69-cf3bbb0cd5cd | -1.2037 | -47.9698 | 2025-10-02 04:27:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 77298b9c-01cc-3e71-8fa3-dc4a5108db31 | -6.05375 | -42.43941 | 2025-10-02 04:27:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3963c6d9-246c-3abd-8592-50b18de42413 | -5.91814 | -44.86026 | 2025-10-02 04:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 549e43f0-d71b-3dfe-a628-7e1ed7ab5051 | -5.15952 | -46.42301 | 2025-10-02 04:27:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 67b0b110-651b-38b8-9dc6-a2657b5dd2a9 | -5.82763 | -42.81359 | 2025-10-02 04:27:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9617fdf9-10c1-3472-ab9d-c418cc2ad405 | -5.9868 | -44.5962 | 2025-10-02 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ca96ffa5-4e66-3285-93fb-abc456544636 | -4.37198 | -43.01299 | 2025-10-02 04:27:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46c7a288-49b8-3c3b-b846-6a5ca4081417 | -5.45454 | -42.84521 | 2025-10-02 04:27:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2e5c7360-d0eb-3900-8933-f5b5eb03e630 | -5.2385 | -46.22574 | 2025-10-02 04:27:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e75dd492-abdd-3591-af7e-c70376a88ea4 | -5.71319 | -42.684 | 2025-10-02 04:27:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ac39c915-4f85-35c5-87b0-06e64097008c | -3.80446 | -51.31345 | 2025-10-02 04:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3800b55c-87d9-3de5-9665-192c71e6615f | -5.27317 | -42.88816 | 2025-10-02 04:27:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3a6eff33-b7ce-303e-9a00-6475d53cad67 | -4.25724 | -48.56073 | 2025-10-02 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fceba6fe-da4c-378a-9701-f4a38cd34e7e | -5.78207 | -42.86727 | 2025-10-02 04:27:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| fb254383-6ae0-3799-a097-6a962f2f463a | -5.27744 | -42.8845 | 2025-10-02 04:27:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 7aad35ec-0a52-3d69-a76b-d6b4265f437f | -5.78683 | -45.74682 | 2025-10-02 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7904b898-1e09-3635-bdb8-5aa489f12202 | -5.20947 | -43.67898 | 2025-10-02 04:27:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0afab94-61a0-3e1c-a0f8-dd392a7a5e35 | -5.2434 | -44.4653 | 2025-10-02 04:27:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 32d28469-3832-3152-a9b7-7af1f303c58d | -4.89668 | -49.96416 | 2025-10-02 04:27:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa19bc66-038b-3f1a-82b2-b4bd3aece851 | -5.81882 | -42.84699 | 2025-10-02 04:27:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 27b13dbb-b91c-3bbb-90db-fd5158a0ffe9 | -3.62294 | -42.77441 | 2025-10-02 04:27:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2810b199-2dcc-3c32-bf65-26374dc8df4e | -5.79538 | -44.91131 | 2025-10-02 04:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3101614-ec80-3e5a-92f6-2d75de7b98d2 | -5.70869 | -42.63827 | 2025-10-02 04:27:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 5828cd19-4914-3a7e-8184-5571ad8ea34c | -5.039 | -42.91089 | 2025-10-02 04:27:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 108d31c6-5b10-33d8-865a-80f50033edec | -2.24884 | -47.88663 | 2025-10-02 04:27:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c159774e-6fcf-39bf-9783-c0fbcafbf9b3 | -5.45519 | -42.84099 | 2025-10-02 04:27:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d205931a-f92b-3c49-badd-bfddc61de3cc | -5.63479 | -45.96147 | 2025-10-02 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85863e6c-89eb-351d-b1f8-19a9a2dfedf0 | -4.00779 | -43.2734 | 2025-10-02 04:27:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7c1dc98-70c6-3602-af25-5292f4d6ce0c | -4.0845 | -50.7528 | 2025-10-02 04:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51585fac-c067-3ab6-afac-93d41dcf0f25 | -5.7947 | -43.07935 | 2025-10-02 04:27:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9e76172a-c234-3ecd-b59f-86b9f239e968 | -5.93899 | -44.85985 | 2025-10-02 04:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 28d34a73-49ce-3b97-953d-8d3df128da9f | -5.17681 | -45.38747 | 2025-10-02 04:27:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 77e193f3-62c6-3727-b140-3cdfebd89a23 | -2.92584 | -48.29968 | 2025-10-02 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 89e2d99a-3c88-3893-9b72-b37159170c34 | -4.31238 | -48.0886 | 2025-10-02 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7421946e-0a0d-328e-a68f-90b90fdf0ad9 | -5.74198 | -45.51839 | 2025-10-02 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 96cdb058-97c4-3f79-947d-92328c494267 | -5.19628 | -45.39411 | 2025-10-02 04:27:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| af2ac485-3e09-3656-b625-3a0ac66d1604 | -5.41031 | -41.34221 | 2025-10-02 04:27:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1a95f320-11af-329b-bbf4-1e51d2dd8b24 | -5.24458 | -43.09981 | 2025-10-02 04:27:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README61.md)
