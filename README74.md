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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e51dd068-bcb5-385f-b1e3-31d5790c840f | 1.20558 | -50.77135 | 2026-09-18 05:14:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae4429b0-36f0-3fbe-b0c7-bce99c17cf63 | 4.00475 | -51.64785 | 2026-09-18 05:14:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39c18a31-fa2f-33ca-b489-655f847e7b4e | 4.00832 | -59.6178 | 2026-09-18 05:14:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9659140d-35f3-3d31-8b52-a7395d5872af | 1.25296 | -50.77801 | 2026-09-18 05:14:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e45a5d46-33ec-316c-bc6d-b322b833410f | 1.25238 | -50.77448 | 2026-09-18 05:14:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f1faa291-666d-30b5-8022-560ab3e2fbbf | 2.47886 | -50.95353 | 2026-09-18 05:14:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 384eb1d7-32d1-3691-9fdf-a4f91e7ae3d5 | 4.10899 | -60.66093 | 2026-09-18 05:14:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e4d85e1-178a-35ee-807d-338205095503 | 1.20502 | -50.7678 | 2026-09-18 05:14:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 584a24a1-9a94-374c-9837-5f8322e61bcf | 1.23601 | -54.68057 | 2026-09-18 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a245cfee-f705-341e-b55d-78bfb9b2d007 | 1.33376 | -50.60872 | 2026-09-18 05:14:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0ed96bfe-620b-3ae9-992b-9cc86db5da72 | 2.09509 | -50.8624 | 2026-09-18 05:14:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d92abbc-33ee-39aa-b742-d5b20cf368e3 | 2.09473 | -60.21578 | 2026-09-18 05:14:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31c6bfea-751f-3108-8c9d-3b60567fcc68 | 1.33317 | -50.6051 | 2026-09-18 05:14:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fa62824a-ef03-3dc0-bec8-1ecf96a9ce5a | 1.33258 | -50.60148 | 2026-09-18 05:14:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2e86f20-6721-3fd2-aada-6c763569fa08 | 2.17168 | -50.94147 | 2026-09-18 05:14:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 937b2062-717f-3a93-8f28-bc5c2e53fa3a | 4.11011 | -60.66845 | 2026-09-18 05:14:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e91c5600-a546-3016-9f51-226bad792382 | 2.09193 | -50.86816 | 2026-09-18 05:14:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f00c08d2-b937-32ae-8ee2-a3f3094dd974 | 1.33725 | -50.60445 | 2026-09-18 05:14:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fcaf0c88-b858-3f28-9621-e2342af18ed3 | 1.28497 | -50.87374 | 2026-09-18 05:14:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7941c7ad-abef-3cd4-a266-93abe2edef8e | 1.33434 | -50.61232 | 2026-09-18 05:14:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6d7e1b2a-ea3a-3075-aa04-92a7b8273e87 | -3.70401 | -54.17709 | 2026-09-18 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac8cb233-a8cf-30b3-8b20-a4d0e8de4b92 | -3.7249 | -60.61056 | 2026-09-18 05:16:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dfe95f7d-3ed5-3382-a93a-1d1bd76a4fe6 | -4.56988 | -54.91643 | 2026-09-18 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 97dd8820-3230-37f7-8da8-776e3582b0df | -4.42824 | -55.44299 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c23da9a2-ffb9-381a-ab43-b9e1cb8633b6 | -6.61622 | -44.20335 | 2026-09-18 05:16:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2e9468d-9063-3601-b984-9831cfa8da52 | -3.43944 | -58.21423 | 2026-09-18 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03cf5508-29b6-3982-8bfe-ebced0781600 | -3.38042 | -50.44309 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3645e873-7a8d-304c-8785-ff259b0ac605 | -3.06528 | -49.52128 | 2026-09-18 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0895b6fa-f538-384b-9b8f-5cad98ae6f4b | -4.50791 | -54.98126 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c52f776-51f2-377a-9f73-b4ffad1e82ee | -1.03296 | -53.74083 | 2026-09-18 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ffdc4e05-a902-3fa7-b091-c63d8df7edb6 | -6.3657 | -58.29241 | 2026-09-18 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1bdf2fbb-2ad8-3ce8-96f1-d0bd61887360 | -4.80534 | -56.08413 | 2026-09-18 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c52818de-c9b8-3dae-9b5d-39ea171eeb5d | -3.43555 | -58.19536 | 2026-09-18 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5bcaefc-a792-3593-9df6-c29b0845ac3a | -2.82677 | -50.47757 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 5daecd6b-0fec-300d-8bf6-950072888750 | -3.4445 | -58.20409 | 2026-09-18 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d1aad1c-0f93-3f1b-8aa3-f30842de762f | -6.6084 | -44.20844 | 2026-09-18 05:16:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3cc60545-558d-3d40-ac8b-281833b235e1 | -6.12093 | -44.02543 | 2026-09-18 05:16:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| beb992da-b3f5-3434-83cf-adf797561d30 | -2.89622 | -57.78155 | 2026-09-18 05:16:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4571c175-2d22-342a-879a-68c355845691 | -6.14127 | -57.69428 | 2026-09-18 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18a67606-d425-3019-8f0e-1956b926ac59 | -7.62883 | -45.84188 | 2026-09-18 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb05b8d0-5959-32bd-88e4-8985c75e07e3 | -3.36271 | -50.44624 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 675ad3fc-8764-3fa6-b371-f24cd24de278 | -2.91711 | -50.41699 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b51738f4-5f3b-3afc-8c67-2fe6cdbea910 | -3.16477 | -48.61123 | 2026-09-18 05:16:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e57aa2d8-1f58-3f5d-968c-1aaff6256c2b | -6.02713 | -51.81199 | 2026-09-18 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b59d6059-7df2-3309-83b5-18ccec80c7f9 | -1.78897 | -47.83777 | 2026-09-18 05:16:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 79b81e8f-57a4-3abd-a00e-13d24100bf12 | -5.86498 | -52.06212 | 2026-09-18 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9a1a7f8-2616-3e8f-b335-ac0e62e6b1c7 | -7.34498 | -44.63784 | 2026-09-18 05:16:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 379b42cd-0773-3270-8e54-d123d79d78ed | -3.70681 | -55.9641 | 2026-09-18 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76040ce4-9d6a-392c-8486-a7c59e58df03 | -7.62954 | -45.83654 | 2026-09-18 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79d05bd3-45e9-3558-b97e-3cfbf1f76ba7 | -2.8215 | -50.48269 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| dec9503f-c0e1-33d0-a7e9-25d25cbd3705 | -1.17942 | -54.17156 | 2026-09-18 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9912512d-408c-3647-9bd2-10a06192cefe | -3.26794 | -54.25964 | 2026-09-18 05:16:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1d43952-7da3-39b7-a6d2-3922081c1fdc | -6.52175 | -58.31403 | 2026-09-18 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b925de0f-3d8e-30e0-a2a0-a612398e3099 | -2.90915 | -54.17084 | 2026-09-18 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc17d7a3-274b-38da-b84b-6f1b01350d24 | -3.92476 | -55.92264 | 2026-09-18 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c0dfed04-23f9-3370-b8e0-6d7f79868f8a | -6.02292 | -51.81141 | 2026-09-18 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3da6ed7-910c-31be-bf8f-2333e9421886 | -6.61485 | -44.20494 | 2026-09-18 05:16:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da5616f0-b7ed-3f8c-97c4-412738a0195c | -2.70094 | -57.59989 | 2026-09-18 05:16:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 10e8c081-03f3-30fb-aa33-c77a70b5033a | -3.04188 | -57.42174 | 2026-09-18 05:16:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8c97cc0-00bd-342f-b7eb-c022847cbeae | -2.89972 | -54.1823 | 2026-09-18 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5a419ec0-833f-3e82-a819-d59a942c72bf | -5.75096 | -45.10205 | 2026-09-18 05:16:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 502579d4-fb30-3dc3-a446-dbf0f17278d9 | -3.70917 | -57.09245 | 2026-09-18 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bbe34071-6964-3cc9-8815-f8b512c2e964 | -7.05978 | -46.22585 | 2026-09-18 05:16:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b852750c-d81f-3452-bcd1-a27d836be483 | -4.51095 | -54.97728 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7cb2eb1e-8e47-35eb-ac9a-ee9cc988fdae | -3.21468 | -53.95058 | 2026-09-18 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 20368efa-c689-3fa0-b95a-faa2f962c919 | -2.68981 | -57.62676 | 2026-09-18 05:16:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0a93a33-49c0-36de-93b7-8ed90324da17 | -3.43947 | -58.19234 | 2026-09-18 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3477627e-8463-3888-9f88-a4c9ed9dd931 | -3.43778 | -58.20302 | 2026-09-18 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3f3d462-89de-3637-a256-8b955b08e1bb | -5.63263 | -44.80512 | 2026-09-18 05:16:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 27c6459d-9169-3d07-b2fc-230fbad060d2 | -3.36578 | -50.45569 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0ccc7ebb-50fc-31a3-b1b0-c82569e948c0 | -2.90828 | -50.41565 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7424b28-1e12-3785-8d18-0af476ce2d6c | -5.75112 | -45.09196 | 2026-09-18 05:16:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| defe0b92-fe03-3923-bfa5-ddaba362f9d6 | -3.96585 | -56.13384 | 2026-09-18 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bebe8b35-35b4-3c2a-a828-3b77dcbceb19 | -7.05775 | -47.4848 | 2026-09-18 05:16:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 135a4068-8382-32c3-ad4a-c63aebfeade3 | -3.54092 | -53.99395 | 2026-09-18 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0c84e94-2c14-347b-b693-d4096cb8380a | -3.97028 | -56.12737 | 2026-09-18 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc9f861f-0dcb-32fc-bfcf-44f1d197c8cb | -7.86203 | -46.43196 | 2026-09-18 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fe86be9d-a174-312d-a557-bbc61216c5d7 | -5.14567 | -55.94787 | 2026-09-18 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1788776f-42cc-364a-bd27-c5ae686c7901 | -2.69926 | -57.61036 | 2026-09-18 05:16:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a5f4d01-9e8d-3f4e-82d9-58cbbad499e3 | -6.32857 | -45.66854 | 2026-09-18 05:16:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d05ade1-fbb9-3f09-b198-22e4b08bd6a7 | -4.56641 | -54.91593 | 2026-09-18 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e5bccc2-2dc1-320f-9cdc-764ce0511f69 | -3.88393 | -58.94627 | 2026-09-18 05:16:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f956db59-1ac2-3c92-82d5-77f2e0a88e86 | -4.3515 | -54.78685 | 2026-09-18 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08d9efa0-3961-383b-9512-827a3e3539ce | -3.43219 | -58.19483 | 2026-09-18 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aec86a9d-a386-3e8f-a3b1-550396c9bc8c | -3.72577 | -60.59576 | 2026-09-18 05:16:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90ab42ae-195c-3066-87f2-257fd8d6a566 | -4.51619 | -56.09029 | 2026-09-18 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99081fdd-1014-3de7-9bfb-594c9b8ad150 | -4.51382 | -54.98163 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 50742c46-71fa-3640-86f7-2436308927b2 | -1.73244 | -55.24304 | 2026-09-18 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38952a96-6c67-35e1-87fb-ed36cf8af2ea | -3.92196 | -55.74453 | 2026-09-18 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c6a801c-f257-3b68-bd02-c0fb1187415c | -7.23039 | -44.21723 | 2026-09-18 05:16:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 400cfb8e-8ccc-37d7-a183-22c9e5760cf3 | -2.61192 | -54.75781 | 2026-09-18 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 5e7cee8f-a2dd-39ac-821c-816da5740eb3 | -3.42883 | -58.1943 | 2026-09-18 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa133522-f44a-364b-9d6e-8b613bd0c2d0 | -7.57782 | -46.35474 | 2026-09-18 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 160337bf-1063-34d7-9ae5-4dc9c8a11750 | -2.48999 | -49.41422 | 2026-09-18 05:16:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa4b83da-d857-3d0a-a149-9425ebe6dabf | -1.70504 | -55.02303 | 2026-09-18 05:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0cd38013-b0dc-374f-a3d1-16a4021a91d3 | -2.67976 | -57.60698 | 2026-09-18 05:16:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5734570a-6001-3c10-97bc-603725338ae9 | -3.44673 | -58.21174 | 2026-09-18 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3818c4b4-ecc2-3042-b0b8-563de430b4f7 | -3.57425 | -43.47049 | 2026-09-18 05:16:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0fe9c2d3-f8f5-3e9f-8d71-c78ed347510e | -5.97846 | -55.36106 | 2026-09-18 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68ba7e55-509c-3fea-ba8f-41857b6575db | -3.56268 | -54.22504 | 2026-09-18 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README75.md)
