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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c7f5a2d-a667-3dfa-b3af-8ded4fbf85cc | -4.21569 | -46.87865 | 2024-10-29 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7006c490-bf9f-3000-8b5b-5d23cbd1071d | -4.21497 | -46.8828 | 2024-10-29 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3d848372-5195-35ba-a51d-ba6252a9371d | -4.21084 | -46.87819 | 2024-10-29 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c027560f-20e4-37f7-aba2-386593634775 | -4.21013 | -46.88241 | 2024-10-29 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 504946e5-2bbe-3684-8dc3-bc112244c62a | -4.50145 | -47.06334 | 2024-10-29 03:47:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ce7ceb7f-0c3c-3a30-bbd5-a9e67bdd99e7 | -4.49936 | -47.06298 | 2024-10-29 03:47:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3376b034-4e27-3d15-a4de-6d44a3b05487 | -4.43256 | -47.6185 | 2024-10-29 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| b3e4200f-9a13-3ca9-9bb4-88ddd2e1ab09 | -3.95716 | -46.41045 | 2024-10-29 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 810badab-8f34-3232-ad57-247babeb76dd | -3.95653 | -46.41408 | 2024-10-29 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f2f507f2-e821-30dc-a3fe-15ae4a469585 | -3.95598 | -46.40773 | 2024-10-29 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 91e15f6d-81a4-3408-a880-9a7c36dde250 | -3.95541 | -46.41111 | 2024-10-29 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 256ce711-05b9-39a3-85f4-d6b304534457 | -3.95478 | -46.41491 | 2024-10-29 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7d08aa6d-3a09-3ba3-ac8d-7128b40c5cff | -3.95203 | -46.40622 | 2024-10-29 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 68f6f78c-f483-32d1-b0d7-7c907dcf318c | -3.95142 | -46.40967 | 2024-10-29 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 66125511-720f-38f4-a916-0de544d65109 | -3.9508 | -46.41324 | 2024-10-29 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 71b4d2e8-3b1a-3ce6-aa3e-513b86e0cd75 | -3.95022 | -46.40709 | 2024-10-29 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dbe9e49e-a5ae-3c23-b5a8-0bc2062f5370 | -3.94964 | -46.41054 | 2024-10-29 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 41f97702-e17d-3adb-8117-90ebdfd32239 | -3.94942 | -46.42111 | 2024-10-29 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a0ebc80-3b5c-33db-a92f-362e0561b17d | -3.94902 | -46.41421 | 2024-10-29 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b6f85741-572b-3a21-afd9-cc43a092e12c | -3.90811 | -46.44757 | 2024-10-29 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0dd7a35d-52f9-3202-b87c-7b59e64cec78 | -3.89037 | -46.34538 | 2024-10-29 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 713e0b68-9006-314c-a361-e86663c44c80 | -3.88973 | -46.34908 | 2024-10-29 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ccf8762-e1ff-3640-b29f-b5f27e33b719 | -3.83096 | -46.48423 | 2024-10-29 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e46fe097-3630-3603-a5e5-fa16b4462500 | -3.82985 | -46.48429 | 2024-10-29 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ec99f17e-7ea0-3349-a4cf-935b3665251e | -6.51404 | -47.0509 | 2024-10-29 03:47:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff4de2e7-5529-3134-92cf-9f33f0e72ebc | -6.50977 | -47.04175 | 2024-10-29 03:47:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5e6f926b-33ee-3363-aa64-60eb1a9c6b84 | -6.50905 | -47.04581 | 2024-10-29 03:47:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 97690d90-9d39-39ba-ac83-749793f8e0f7 | -6.50834 | -47.04985 | 2024-10-29 03:47:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 34f539de-d10a-36b5-b6f8-8d502415ea05 | -6.50334 | -47.04483 | 2024-10-29 03:47:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 72769623-19a9-3b78-b5f7-b764981e6eed | -6.50263 | -47.04883 | 2024-10-29 03:47:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a02ba8dc-571c-3285-a512-095b58cb01c7 | -6.29432 | -47.34589 | 2024-10-29 03:47:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c53c165f-2051-303b-9e59-e5b444ac2a10 | -6.29356 | -47.35007 | 2024-10-29 03:47:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40c9fd5d-7764-3705-8222-5a58e8d2667e | -6.62689 | -47.35713 | 2024-10-29 03:47:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 065f6ec5-f00e-35ef-8eb1-e5dc94946767 | -6.60843 | -47.39267 | 2024-10-29 03:47:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3ca0948-2549-3648-8b9e-dbee46296db8 | -6.60767 | -47.39687 | 2024-10-29 03:47:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c263f3dc-078c-3114-a30a-fbe2c31e7ec0 | -6.60306 | -47.39346 | 2024-10-29 03:47:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| afb4ecb5-d77d-3854-a9cf-dbc3a9f9b827 | -6.60261 | -47.39164 | 2024-10-29 03:47:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| fb859915-e7ef-3889-8c9d-cce90ea6ac09 | -6.60234 | -47.39761 | 2024-10-29 03:47:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| e29c42f6-3797-3e89-809a-76039a450076 | -6.60187 | -47.39568 | 2024-10-29 03:47:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 61a25644-0c35-33a6-befd-5db486b1e494 | -6.60109 | -47.39997 | 2024-10-29 03:47:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| a440d9c8-d558-3bd0-9fcd-747e0b518148 | -6.59727 | -47.39221 | 2024-10-29 03:47:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| ea397c2c-4038-3e6a-83bb-b4690b74e469 | -6.59657 | -47.39621 | 2024-10-29 03:47:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 18938fe1-50c0-3be3-818e-645a58c7f45e | -6.59609 | -47.39442 | 2024-10-29 03:47:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| ff886543-2167-3c92-b4db-db45039d1ef2 | -10.44338 | -49.04969 | 2024-10-29 03:47:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 58c84da5-a8a9-3eea-a277-ed68d4114687 | -10.44251 | -49.05418 | 2024-10-29 03:47:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7ad864c0-d796-34fc-a0ba-b65e1bd13f52 | -11.96857 | -48.09616 | 2024-10-29 03:47:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9015dfb7-2c54-3e07-98c2-b475e5713430 | -11.96802 | -48.09242 | 2024-10-29 03:47:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31501df0-ad6e-33ee-9523-d71001486a32 | -11.96729 | -48.09613 | 2024-10-29 03:47:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d0a6146-3716-3d55-b2a7-60624b644c8a | -11.96377 | -48.09112 | 2024-10-29 03:47:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38d214fd-0c0b-3e0c-a61d-279949da2fc2 | -11.96307 | -48.0948 | 2024-10-29 03:47:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cfab03a5-8260-3596-96aa-5e0e77043227 | -11.82345 | -48.75914 | 2024-10-29 03:47:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3ac5173-3687-3aca-a0f0-43b072e8eb63 | -11.82297 | -48.76388 | 2024-10-29 03:47:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85a23d6d-446d-3d2a-b3fb-83dac2661243 | -11.82261 | -48.76332 | 2024-10-29 03:47:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b40ec19-4a88-383e-8707-9d36b2fd7458 | -11.81798 | -48.7585 | 2024-10-29 03:47:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 19598930-c64e-3f7f-b805-fe8e9c3b6cbb | -11.81765 | -48.75797 | 2024-10-29 03:47:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce2f073a-8003-3331-918f-1825dc6bd5c1 | -11.72192 | -48.36171 | 2024-10-29 03:47:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6948297c-a36e-3e1d-8366-d12cc136fb98 | -11.24326 | -47.90385 | 2024-10-29 03:47:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e541a8f7-3d4c-317b-9e0d-42a0ba0cbcb9 | -11.24255 | -47.90766 | 2024-10-29 03:47:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a84a6c1b-cb7a-31d5-bd6d-e2f09ed54d35 | -11.24183 | -47.91148 | 2024-10-29 03:47:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 90230978-2aea-3239-b253-f973ef820e96 | -11.24156 | -47.90464 | 2024-10-29 03:47:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 031846ae-ddf8-39b9-80d4-9045e28411b1 | -11.24082 | -47.90842 | 2024-10-29 03:47:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2762c726-05b3-3538-9ed2-020600e66f6a | -11.23697 | -47.90667 | 2024-10-29 03:47:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 22752157-a4a9-35f9-b6ca-142098e5345c | -2.18197 | -47.95716 | 2024-10-29 03:47:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5ef1151-bf81-3d5b-aa85-127dfab111e0 | -2.17639 | -47.95075 | 2024-10-29 03:47:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d663462f-a752-31e2-a798-dfab49b49b4a | -2.1755 | -47.95615 | 2024-10-29 03:47:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 903247f4-3a86-39bb-ab86-25ec7e0e1e6b | -1.9779 | -48.688 | 2024-10-29 03:47:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56bab08f-168a-3ab1-bfb3-4e33f797d87a | -1.77487 | -47.84205 | 2024-10-29 03:47:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| eacd5de5-a93d-3cb0-a1eb-036e6edec2e3 | -1.77468 | -47.84082 | 2024-10-29 03:47:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c1446b5-d614-3bd1-89f2-7d05b0356c35 | -1.77379 | -47.84624 | 2024-10-29 03:47:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d5fc8088-faba-3ff9-83c9-df8b278f9611 | -1.67364 | -47.38947 | 2024-10-29 03:47:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1388f0a9-0d51-3a3e-8e9e-7eab0d783d9f | -1.67284 | -47.39448 | 2024-10-29 03:47:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 101c92b1-f698-312f-b8e0-fda1ae982a8c | -1.6703 | -47.39024 | 2024-10-29 03:47:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f42cce25-ff8c-31ce-aa2f-ac95562e2f02 | -1.52552 | -47.20757 | 2024-10-29 03:47:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9afdd525-1a88-3864-bca7-62fc97807e68 | -1.52473 | -47.21238 | 2024-10-29 03:47:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c6f78afc-3523-3be4-9715-05e032cdfdb2 | -1.51932 | -47.20635 | 2024-10-29 03:47:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f51fd4b-7bcb-3190-91dd-8618384c5e07 | -1.51851 | -47.21129 | 2024-10-29 03:47:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c69e276-a182-352c-91f9-2c4d701a0400 | -2.97177 | -48.06059 | 2024-10-29 03:47:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 67d8ec1a-0a9c-3ab7-bc18-11d9bde1d47a | -2.96536 | -48.0594 | 2024-10-29 03:47:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d38c129b-02ea-3b6e-ae74-8660309235dd | -2.96445 | -48.06471 | 2024-10-29 03:47:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f44ec562-4abe-3473-b1fc-b74df4e00d60 | -2.94045 | -48.56266 | 2024-10-29 03:47:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ad63802-f630-389b-add2-3d7707926f08 | -2.93949 | -48.5684 | 2024-10-29 03:47:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c4eb72b-d872-3e0a-9592-3bc747c8782f | -2.61173 | -47.94444 | 2024-10-29 03:47:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 051fc2c0-1efd-3249-a6f1-91e1fc703f1e | -2.61082 | -47.94968 | 2024-10-29 03:47:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d50d8492-a000-3163-9be4-a3a454e15762 | -2.61003 | -47.94826 | 2024-10-29 03:47:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 39d114e6-dc02-32e7-ba78-a6c7c5c91915 | -2.60364 | -47.94702 | 2024-10-29 03:47:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8aa5db42-a471-3273-bed8-055ee6e4d422 | -2.52307 | -47.45549 | 2024-10-29 03:47:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3d819d3e-061b-3865-a818-fb79279b5f2c | -2.52239 | -47.44646 | 2024-10-29 03:47:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eb36a4f2-bc18-3013-b271-157201cb28dd | -2.52224 | -47.4606 | 2024-10-29 03:47:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e0b5006-955c-3a68-a53d-24d3de83fc8e | -2.5207 | -47.45645 | 2024-10-29 03:47:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 51ecad1b-93c7-3413-8605-fe53f5a77725 | -2.51848 | -47.44432 | 2024-10-29 03:47:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ac7e0bb1-a4fb-3c35-8de4-66fb1b638d6c | -2.51766 | -47.44932 | 2024-10-29 03:47:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 465d7b7b-8de3-3ed1-a77e-e21ea793b10f | -2.51685 | -47.45431 | 2024-10-29 03:47:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c2c77580-4652-362e-ad1e-3de152addca3 | -2.51616 | -47.44542 | 2024-10-29 03:47:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| b6d92853-d8f1-3e87-b48b-c9aa558f38d8 | -2.51604 | -47.45928 | 2024-10-29 03:47:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ff33285-05ed-33df-848c-067b212e17d5 | -2.51531 | -47.45039 | 2024-10-29 03:47:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 523c28b5-3e1e-35ce-a7be-f0c6c6560849 | -2.51447 | -47.45533 | 2024-10-29 03:47:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 10fecd63-dfa8-3671-b63f-f4bdc0f473af | -2.51142 | -47.44831 | 2024-10-29 03:47:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 40ef5d19-13d7-386d-9609-f2e5d58a7b2f | -2.51062 | -47.45325 | 2024-10-29 03:47:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| c8457275-8f2a-3568-9aa4-8a0d927908cf | -2.50981 | -47.45823 | 2024-10-29 03:47:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| d42c7a6d-32be-3a5f-bdbd-cb58dffeac78 | -2.50908 | -47.44933 | 2024-10-29 03:47:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |


[Clique aqui para ver as próximas entradas](README31.md)
