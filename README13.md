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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0cba5849-b74f-3866-a07a-ee55c156ba42 | -10.53239 | -42.54956 | 2025-08-13 03:49:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e00979b9-236f-397a-a1fd-e39e2474cfe9 | -12.49282 | -46.95964 | 2025-08-13 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc7c40a5-b34f-3e75-af12-2d010af6801f | -12.5075 | -46.96562 | 2025-08-13 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 588cd0df-96ca-37e2-9256-94f30ffca9ae | -11.71468 | -51.61523 | 2025-08-13 03:49:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b72103a-53ca-35fb-815a-4650976ba7cc | -5.18235 | -37.65923 | 2025-08-13 03:49:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1f8b38d5-ce1e-3b33-8e9c-5e1b38d70aaf | -9.7064 | -49.48005 | 2025-08-13 03:49:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a030144a-f2ee-3ceb-b747-db7c1b30212a | -12.48655 | -46.96484 | 2025-08-13 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 200f5843-70ea-373f-9251-4dfb7d826f78 | -12.50182 | -46.96775 | 2025-08-13 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92781b8f-b682-3cf0-9e6f-9e82567fe2f1 | -4.16859 | -42.45 | 2025-08-13 03:49:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a20028b9-9251-3566-b505-4051ff3b4e99 | -9.84646 | -47.82522 | 2025-08-13 03:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| bcf5ea0d-2b78-3a8b-a6f0-a9adca31d667 | -4.22486 | -47.21606 | 2025-08-13 03:49:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 78171940-90fc-371f-9ac5-b2964656f555 | -13.53544 | -47.62529 | 2025-08-13 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e68af8e9-08b0-3104-9a81-dfd0bfc4adda | -3.3755 | -47.6125 | 2025-08-13 03:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eef17781-3372-3f03-a839-5744cdb038a2 | -4.40438 | -47.6314 | 2025-08-13 03:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95204191-761f-3662-9d07-5b19f4492eb5 | -9.77851 | -48.36912 | 2025-08-13 03:49:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e45709c7-f6fa-33fb-973e-2b4082a29305 | -10.33948 | -50.82199 | 2025-08-13 03:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71fae68b-f032-385b-a228-570c8300474a | -14.12297 | -44.31423 | 2025-08-13 03:49:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67e38aa4-f72b-3610-81f8-ac54c7865a69 | -9.77401 | -48.36788 | 2025-08-13 03:49:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 315918ba-60fa-3792-9ea3-dd76fa5bbdb7 | -5.18569 | -37.65976 | 2025-08-13 03:49:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 6cf9e7a0-3c1a-349f-85c4-936e0058afeb | -14.12043 | -44.3133 | 2025-08-13 03:49:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1d11a52b-862e-34dc-aef5-4d9ddd4ebbe7 | -12.49791 | -46.96061 | 2025-08-13 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1f61148-4dce-3b6d-bdb8-2a033a052ac7 | -11.45373 | -47.32658 | 2025-08-13 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e56484d7-f630-3dbd-9620-c023db1e0602 | -10.75446 | -48.78146 | 2025-08-13 03:49:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef3db933-b090-3b1d-8ec1-ade2f57a96f8 | -12.50241 | -46.96468 | 2025-08-13 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2d8cafd-591d-3f7d-8659-eeda763a32e9 | -16.39951 | -50.89124 | 2025-08-13 03:49:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2652a627-9712-314b-8266-f869fecbd413 | -11.75983 | -48.19711 | 2025-08-13 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 900066f5-a572-3e94-b90c-9e1065078409 | -6.12679 | -44.71458 | 2025-08-13 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c953c4e0-7d2a-3c4f-b419-b32f01952545 | -5.31962 | -45.22281 | 2025-08-13 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b57009d4-2748-302d-9151-76bb911962cb | -10.96637 | -49.57628 | 2025-08-13 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 18f1c97c-acd1-3fed-883f-7bd5ab9dd8b9 | -16.2923 | -48.01441 | 2025-08-13 03:49:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a79531db-cdf4-3085-8490-5790f4858d76 | -11.75795 | -48.19577 | 2025-08-13 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| feb6befa-1bab-3128-8bc5-f49df8a0f16d | -13.76576 | -42.62132 | 2025-08-13 03:49:00 | NOAA-20 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 66343f8f-b176-3f33-89c3-2e21f4baffb7 | -10.49834 | -42.42118 | 2025-08-13 03:49:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 79992b8b-e95c-3694-b554-4cc2eafe45f5 | -11.96676 | -41.68506 | 2025-08-13 03:49:00 | NOAA-20 | MULUNGU DO MORRO | BAHIA | Brasil | 2922052 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3e4e0685-da63-358f-a333-d459b84f97d2 | -13.53029 | -47.62394 | 2025-08-13 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b7571d6-e0f5-3c15-98e9-cc0afbe96192 | -12.5431 | -46.97261 | 2025-08-13 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca5a5835-6505-38e2-97b5-3be7a8112a0d | -12.50299 | -46.96159 | 2025-08-13 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f6cae84-f8ed-380d-98ab-6932b7a6e342 | -9.6589 | -48.15163 | 2025-08-13 03:49:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5b245fe-404a-3ad0-9681-426d4cdd5999 | -12.49223 | -46.96273 | 2025-08-13 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb758273-3833-3e6b-b69f-1421a807403b | -5.18291 | -37.6557 | 2025-08-13 03:49:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cf94664d-fbb7-3cde-9fda-fb5839c34459 | -16.91228 | -48.14921 | 2025-08-13 03:49:00 | NOAA-20 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d838fef-cd5d-34c1-a3f1-923fd91a1eb6 | -9.77268 | -48.36793 | 2025-08-13 03:49:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b56a995f-63ba-3f42-8de8-942a680854ac | -13.53605 | -47.62218 | 2025-08-13 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d8bba0f-b1c1-3e8c-932e-3b4ab7f0c0c9 | -6.12586 | -44.72013 | 2025-08-13 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 26784928-0d49-3804-913b-d3af157bc921 | -11.71606 | -51.60851 | 2025-08-13 03:49:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e651877-6996-372e-8a33-82d19eaf1053 | -15.09123 | -51.3544 | 2025-08-13 03:49:00 | NOAA-20 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f81fdaa1-e70d-3fd1-8cb0-46626db5b594 | -12.57925 | -46.99232 | 2025-08-13 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| adb848d8-5082-309b-8234-846ff2d66d50 | -12.57765 | -47.05586 | 2025-08-13 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bcee8bcd-e651-30af-9f2a-7cf6bece59fe | -10.96737 | -49.57131 | 2025-08-13 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ef867791-b656-3fda-8b51-6ba36d259bcd | -16.39318 | -50.88903 | 2025-08-13 03:49:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85b8c6d7-8d9a-33a7-8fd3-2e79c0cb3d7a | -9.7127 | -49.48111 | 2025-08-13 03:49:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 44fe2adb-f7a7-3f20-b09b-addd532df027 | -4.77305 | -45.32523 | 2025-08-13 03:49:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8a76310-caea-337f-913c-66d9719a2142 | -14.11744 | -44.32116 | 2025-08-13 03:49:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7f775399-515d-33a6-9bee-d3969e704d7d | -9.84084 | -47.82406 | 2025-08-13 03:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| fec357aa-2761-3eb6-b171-582072b22828 | -3.3763 | -47.60767 | 2025-08-13 03:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9adaf20-9021-3344-bdff-df246c62f44d | -15.08373 | -51.35827 | 2025-08-13 03:49:00 | NOAA-20 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5f0ad5a9-b82b-340c-a2b2-38425a0078c3 | -16.40033 | -50.88522 | 2025-08-13 03:49:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 399f019a-a8f6-33f0-847c-25d5cc66144f | -13.52964 | -47.62723 | 2025-08-13 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4644e5a-9df4-3a92-a365-21cd23753335 | -16.9072 | -48.14824 | 2025-08-13 03:49:00 | NOAA-20 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5337def1-affc-3deb-97c2-24916f13e359 | -13.57378 | -46.95173 | 2025-08-13 03:49:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 665219aa-c57a-3c4a-ad5a-c577a6937fe6 | -10.75361 | -48.78585 | 2025-08-13 03:49:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57a47582-3ffc-3ed5-8874-a815f30eec79 | -11.89884 | -52.53661 | 2025-08-13 03:49:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9ae1c5a-b45e-39dc-947f-8af725028518 | -4.77361 | -45.32196 | 2025-08-13 03:49:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43dfc476-0604-32b2-805d-dcbccadbe637 | -14.11813 | -44.31729 | 2025-08-13 03:49:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| da1f41d2-bf44-3e40-a5dc-81bf057a1429 | -12.14144 | -48.01572 | 2025-08-13 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89550754-7baa-3cdc-844b-d3622e5c992f | -12.14071 | -48.01942 | 2025-08-13 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb22ee71-3d95-3fc7-a559-9507e87abb6f | -12.58317 | -47.05473 | 2025-08-13 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a66b5c02-c590-327e-bf2b-9fbfd8e05ec0 | -5.05049 | -37.71877 | 2025-08-13 03:49:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dcff22b7-308e-37df-9972-258e335c4b85 | -12.57709 | -47.05875 | 2025-08-13 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f8dd8c8e-8075-38a7-bafb-ed8ef92029ea | -11.45437 | -47.32326 | 2025-08-13 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3717a452-5404-34b9-b815-ac901072e6c5 | -13.53928 | -47.63327 | 2025-08-13 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8814ee31-006b-3766-bc77-93ee7226eb93 | -16.39941 | -50.88951 | 2025-08-13 03:49:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43892da4-00c2-38aa-bd0d-9a57e8d77d12 | -13.43598 | -44.50444 | 2025-08-13 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ffc4acbc-78d6-3cdf-a463-9897f91bd39b | -3.3747 | -47.61061 | 2025-08-13 03:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4d0e5e50-117a-361d-8761-692e2581625b | -12.68754 | -46.9653 | 2025-08-13 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 89daa1ec-5471-3251-9076-c91ce8f52a91 | -16.26813 | -47.88042 | 2025-08-13 03:49:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 349e1ae6-6fa7-387f-9236-3d3a8e5f8f61 | -7.22201 | -35.77018 | 2025-08-13 03:49:00 | NOAA-20 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c7218779-df82-33d3-b480-8f47a6b01ee9 | -16.51091 | -47.85329 | 2025-08-13 03:49:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 417604fc-87f1-39c1-ab19-05150dd33410 | -13.62694 | -46.9167 | 2025-08-13 03:49:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36083860-fb67-32a6-9c83-f909dbff81d1 | -11.45967 | -47.32433 | 2025-08-13 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05c1cfc5-bb41-3b43-9130-a3fe5bb71602 | -14.11971 | -44.31717 | 2025-08-13 03:49:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8d798bc8-fb14-38db-8569-400fa4ca8052 | -12.67783 | -46.96108 | 2025-08-13 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb5fb0d7-030b-34e7-9a2a-7d3bbc5fa2bc | -11.76426 | -48.19321 | 2025-08-13 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ea21b38c-e21f-3693-b5f8-b10fc8b3b701 | -12.42093 | -48.69764 | 2025-08-13 03:49:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3b984820-23f5-3b4d-83f2-76de6df5112d | -12.49732 | -46.96371 | 2025-08-13 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e5a7e6f-75c9-3bf8-8553-abdcf158412a | -3.5843 | -47.52943 | 2025-08-13 03:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 17e801be-41ba-372d-8b4a-d206e90e183b | -5.26458 | -36.17355 | 2025-08-13 03:49:00 | NOAA-20 | JANDAÍRA | RIO GRANDE DO NORTE | Brasil | 2405108 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 573700a2-985d-3756-8840-01afb5d65ef4 | -9.65812 | -48.15573 | 2025-08-13 03:49:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8814211c-1961-376b-8028-41136f2ec0fb | -16.51152 | -47.8503 | 2025-08-13 03:49:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c924c29-3407-3c66-9b65-4a37520b2074 | -10.74295 | -48.18724 | 2025-08-13 03:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a4d87b90-1bd3-3f5d-841e-752403ac4936 | -4.17793 | -42.44729 | 2025-08-13 03:49:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9dc27a69-61f2-3593-9aa5-65a4eccf7450 | -13.43674 | -44.50036 | 2025-08-13 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a9d2e99c-7905-3562-8b4f-0b8cfa070e86 | -10.96022 | -49.57498 | 2025-08-13 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c5717e17-2f40-3977-8e35-2103d3fb4683 | -11.76611 | -48.19453 | 2025-08-13 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6fc825dd-e526-3405-8713-f04900ae3dac | -16.96562 | -48.42054 | 2025-08-13 03:49:00 | NOAA-20 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4797500-ea47-385a-8a01-6e0577d88129 | -12.4981 | -46.9666 | 2025-08-13 03:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 438178d1-408b-318c-8210-ab8fb99d24d1 | -7.1299 | -60.1182 | 2025-08-13 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 42845bfd-1d11-37e7-852f-e911f99e68ab | -8.106 | -55.5701 | 2025-08-13 03:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 27c801f7-46a7-3d0c-ba4c-c89cc81dfa6a | -18.06021 | -46.01897 | 2025-08-13 03:51:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c996115a-e506-3b3f-b682-8d2a222e521d | -17.6124 | -46.70506 | 2025-08-13 03:51:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README14.md)
