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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f179f56d-5c27-3838-815f-25347648cc5b | -11.39962 | -45.59432 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f35d41a1-a0aa-350e-bbfb-9b87317da762 | -7.39536 | -47.37008 | 2025-09-11 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9a6810f3-fb65-31da-8e37-a49f2958cf41 | -6.85642 | -47.87602 | 2025-09-11 03:55:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c7d36eea-5c21-372c-be26-63a3599c57ee | -11.099 | -48.44545 | 2025-09-11 03:55:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02c4829d-04d9-3448-9ca6-e2bed789146c | -11.1592 | -45.30389 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 48d93461-8fd1-3ef4-b535-cde200954384 | -11.48481 | -43.63943 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9523ff96-0f0e-3204-ae3a-85a6c189a74a | -7.20304 | -44.96368 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2a9490cc-1e22-36d9-8547-dd7a7ab5c9e6 | -11.78375 | -50.5769 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ac3f610-6de7-3a5f-bc68-9a2d3eefa391 | -11.31625 | -50.76082 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 73c5c775-72c8-305a-a396-a188cc4661dd | -12.05174 | -50.9446 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b1f3d268-f589-38d6-8775-2abbe4c40bb9 | -11.61541 | -46.62843 | 2025-09-11 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 596c0a1b-a862-3583-91dd-716aa0d8492e | -9.68 | -47.52628 | 2025-09-11 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 20740f48-02c4-3c4e-9765-8160830644fc | -8.19367 | -50.10848 | 2025-09-11 03:55:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6b5ad809-0d23-3f59-a2a7-4e79bacc9e0e | -12.01573 | -47.60115 | 2025-09-11 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 86372f0e-6786-34d8-b881-c859d281d657 | -10.895 | -47.7723 | 2025-09-11 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 56e53470-ab82-324e-9de6-97d57f653b60 | -12.59009 | -44.79107 | 2025-09-11 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 986857cf-b1fa-3461-95ac-4c15052afb32 | -11.11349 | -48.39767 | 2025-09-11 03:55:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a406569-8126-3906-b9f7-56a029a826cc | -12.47185 | -47.49194 | 2025-09-11 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| aa3e2df3-de78-37c4-afb8-ccf1fa05d3da | -8.51765 | -45.68602 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6cc6b8b6-9c40-33e4-8e87-d1b69875031d | -12.03673 | -47.54262 | 2025-09-11 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| daa8e14a-24b8-323b-be6e-16b08950683d | -6.69999 | -44.94179 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0d995a81-3fa2-361b-910c-8a98d342acb7 | -9.06144 | -47.05581 | 2025-09-11 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5e3c9526-a4b8-3e90-8872-b32b14e170a2 | -11.42248 | -43.56838 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a0dc30dd-222d-3f0e-b9df-8efc0b71b317 | -11.47731 | -43.63807 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 52535f64-5fea-3857-8c18-1d703d170d9a | -13.1611 | -45.28622 | 2025-09-11 03:55:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b2ab9253-b967-318c-8a17-8f7994d47fca | -10.66821 | -48.62728 | 2025-09-11 03:55:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91a4414f-1c13-3a57-a676-c88f50d00cba | -8.87371 | -49.56748 | 2025-09-11 03:55:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| d1e89380-aecd-3793-b045-52b7b8de44ac | -6.83743 | -45.60695 | 2025-09-11 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6a05049c-7cda-34b5-a21b-3c7a590c2f3a | -11.37087 | -46.57115 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e935274e-d79b-35c7-8276-5198f1fd1a79 | -6.24487 | -43.4903 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0d8cefe4-9475-39c9-9161-91fe272bb374 | -9.12763 | -46.19275 | 2025-09-11 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 22161bde-75db-3a19-a190-c53e56030562 | -11.35771 | -46.54088 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2ce09b45-f265-3f14-a719-6b9aadd79af8 | -11.94366 | -46.64254 | 2025-09-11 03:55:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42a5d882-98b1-3b59-b35a-0b24ad501d7d | -11.74679 | -46.52804 | 2025-09-11 03:55:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e1dbc94f-c648-3d58-b4f0-71c6553cef66 | -9.06889 | -47.07062 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8166fd12-25a4-32eb-8dce-f15e358f667a | -8.97075 | -46.06602 | 2025-09-11 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4579b5cc-b68b-3fb0-ba0e-dda239cc34e4 | -13.01471 | -39.74187 | 2025-09-11 03:55:00 | NOAA-21 | AMARGOSA | BAHIA | Brasil | 2901007 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1da93788-34d7-3357-a615-318f5cbc7073 | -11.16007 | -48.34811 | 2025-09-11 03:55:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b4d80593-83cc-3e18-ab39-27a3b1bbfec4 | -6.31089 | -43.41512 | 2025-09-11 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6657365a-4c7d-3932-9567-02805d814456 | -11.30902 | -50.74878 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90970e4d-b833-3787-b64a-c767b17810de | -7.5357 | -44.67441 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 48d6dfad-09c1-38c5-aa37-1b226e14bca8 | -11.49152 | -43.64541 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 50b99167-8657-364e-90a2-60433d1e84f5 | -9.05063 | -46.97533 | 2025-09-11 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 0e488a1f-7c80-3a6b-92b4-0e32a24a45f2 | -7.54124 | -44.66743 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e4c35ddd-9657-32e9-bb7b-39afa3c76cf6 | -8.1664 | -46.08044 | 2025-09-11 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca71bf4e-060a-3762-bf6b-724329e40b97 | -6.32232 | -43.44559 | 2025-09-11 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b0635a8-7ae1-318e-8e1b-688bfa2508a8 | -13.29876 | -43.75454 | 2025-09-11 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ee717d5-b1ca-361b-8347-48c9ad5d9e37 | -10.38468 | -50.52255 | 2025-09-11 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 38296abc-0c2e-37ca-9e4e-bb04024c3704 | -12.03287 | -47.61562 | 2025-09-11 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 65eb43fb-52de-343f-b79f-56c95258e6eb | -5.8393 | -46.15671 | 2025-09-11 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b18db4a9-49e9-390a-86f1-3cc99dd7dfbe | -13.25202 | -43.78318 | 2025-09-11 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ef19d45-dde1-3331-954c-2d1264b64ceb | -11.97404 | -51.11266 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9ab14556-026e-3059-9173-2f2be9e893fc | -11.43061 | -43.57305 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95bc7a71-7f10-30a9-97cc-b02a47964d86 | -7.91841 | -44.87737 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d7bf6c5-36f6-340a-ba63-5dcf4026a474 | -12.01851 | -47.5885 | 2025-09-11 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3de21508-5836-3ff4-801a-a3c86f11cee1 | -9.20248 | -51.81421 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 70759a88-99f3-398e-b5b6-2f1ec49bc03a | -11.09834 | -48.44892 | 2025-09-11 03:55:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 90aac2aa-a18a-3677-962a-5689b7cea4c2 | -6.31544 | -43.41237 | 2025-09-11 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8bca943-81ce-324f-9bde-204b8d484cf5 | -11.53549 | -41.72934 | 2025-09-11 03:55:00 | NOAA-21 | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ed8c57fb-561f-38eb-82c7-2d88fe2641bf | -6.17518 | -41.07762 | 2025-09-11 03:55:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 148d20cb-e64a-3c67-8dc1-f3df14350de9 | -7.18118 | -44.96021 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cf6edff6-2b04-3d51-81ef-3bbc0f9a98d3 | -11.14595 | -45.28154 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b3c180e2-5c9c-3bf8-bcb2-48b32ceae5d6 | -9.02175 | -49.77053 | 2025-09-11 03:55:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2e9d0992-8549-3bab-8139-23605b4a1875 | -6.55398 | -42.92051 | 2025-09-11 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 231319d5-60d1-3bfe-a563-ac6a067dfc41 | -7.84284 | -45.40399 | 2025-09-11 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0db87af2-9aba-3fba-9260-7a0f0bad6ac8 | -11.82549 | -46.74734 | 2025-09-11 03:55:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2683c750-2b04-3d7a-857b-177d834ee2ee | -9.06919 | -47.08433 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 6be0aa0f-3dda-3e9f-afa6-438868733149 | -6.7339 | -43.98953 | 2025-09-11 03:55:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f94f957-22d0-30dc-a17c-f0095514e777 | -8.35951 | -44.83871 | 2025-09-11 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 60094ac6-f26e-3a79-a857-e44d59935492 | -6.9012 | -47.92096 | 2025-09-11 03:55:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e83d1f73-aa39-35a0-906c-b5bed507f459 | -6.91202 | -44.55497 | 2025-09-11 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 43f518b4-430a-3282-861e-90311b4b5dfb | -9.34285 | -48.94559 | 2025-09-11 03:55:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 63b47430-1160-3253-8ee8-dbf90ebd0eb0 | -11.08508 | -51.33102 | 2025-09-11 03:55:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| e151ed9e-758f-3ddf-aa6b-3fbea761d14a | -6.53032 | -44.60685 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9bb49f9d-8c67-33bb-973f-336d6eb1ee37 | -6.66418 | -44.12458 | 2025-09-11 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e729f5b-135c-34f3-a304-861eed0a7ea2 | -7.71863 | -44.80016 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8eb5d512-9157-3b1a-9a99-11aef7f0d0c0 | -12.42481 | -47.79752 | 2025-09-11 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d71d25f0-a6f3-3368-81d7-c2fc6d808967 | -6.69928 | -44.94601 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 70dc0b85-ffd5-3d8c-8ae2-5e9397e942d5 | -9.02098 | -49.77474 | 2025-09-11 03:55:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5a81ac37-d634-302a-a61b-bc960ef6b820 | -7.46809 | -45.29006 | 2025-09-11 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e1cf738-726f-3497-b6b2-412bd6ed9f97 | -11.47514 | -43.62813 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a70eaf76-9a6c-33b4-b849-871fcf94eee8 | -7.49023 | -48.25119 | 2025-09-11 03:55:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f4814267-e8d6-311e-b81c-8f88c851bbe2 | -11.34947 | -46.52668 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1ab50f22-f202-326f-a0b9-5c1bcff829f5 | -12.03388 | -47.61024 | 2025-09-11 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ae85a25e-151d-37e0-b081-29825703e094 | -11.10667 | -48.42419 | 2025-09-11 03:55:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1bd74589-46cd-38b8-b481-c25d764d4616 | -11.40317 | -45.59907 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9eb14b1c-c9d6-31a1-923f-a6d549702eb4 | -11.09708 | -48.4474 | 2025-09-11 03:55:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 523ebe20-8931-3c2c-8596-9c1816aa6d23 | -11.42982 | -43.5776 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e01efd32-43df-3ca6-9e5a-74ffe445ce37 | -6.564 | -43.14874 | 2025-09-11 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6518000f-7bdb-38a5-ae72-3dc108ba2830 | -9.01695 | -49.76147 | 2025-09-11 03:55:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b80a5918-f149-31d6-a2dc-54dbdd63caad | -6.22121 | -43.37405 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f7db9728-64d3-3ba4-aba8-7cc00186d9a3 | -11.16269 | -45.3085 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fc3ca796-ca22-357f-b6ff-0d66d1e1cbac | -6.32015 | -42.21352 | 2025-09-11 03:55:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 08cf7ac2-1c0e-3285-8830-6525883b6f60 | -11.36145 | -46.54594 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 0fc0d645-1782-31f5-9f5d-d1bac54b3e4e | -5.51573 | -45.45129 | 2025-09-11 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a414c27-ebc3-3be5-b521-dea917e46dc8 | -11.34175 | -46.49133 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 70e5b2a4-161d-33e0-818f-07c18ce7d48c | -6.53852 | -43.10862 | 2025-09-11 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e6fa8614-2c64-3def-ad4e-b7988104ba82 | -11.47573 | -43.64737 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8716b161-9254-3c9b-8bf9-4b91a294745b | -11.63275 | -46.76825 | 2025-09-11 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 319b53bc-9b68-3790-bcec-01d0a6b77a85 | -6.31032 | -43.41854 | 2025-09-11 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README16.md)
