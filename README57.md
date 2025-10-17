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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ee9bbbf-9c91-37b7-965d-7e095ea5c089 | -6.55938 | -48.04646 | 2025-10-17 04:19:00 | NOAA-21 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81ac2558-ef02-36ed-9501-2b571bba5d24 | -5.91228 | -44.74265 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 544a7366-b4e4-3979-b72a-70628e465124 | -10.27575 | -44.04235 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6dac4644-a395-3357-95e1-7a992f36feed | -7.10086 | -41.46246 | 2025-10-17 04:19:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ff0e930c-638d-3786-93f7-809f864a9bd6 | -10.17531 | -44.7861 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| ec10ee92-8dac-34a1-a78c-bc74affa18f3 | -5.29394 | -47.93269 | 2025-10-17 04:19:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 83a29842-0e86-396a-9785-fa2ac6b78621 | -6.32234 | -44.31731 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 71710142-c8cc-35b4-ac3b-8152ee2bcfe5 | -10.17682 | -44.53333 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fa8c4c9b-c700-3b8d-9c63-4134c299a73f | -10.63789 | -45.2259 | 2025-10-17 04:19:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 731ab270-4f7f-3040-baa3-a7de04ad683c | -7.17262 | -42.51519 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8529d0a4-fc67-349d-b7bc-966c1f27d9ee | -6.32947 | -44.31489 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 339bd145-2c89-3555-89b2-35ef0b14e578 | -6.93252 | -45.13812 | 2025-10-17 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a506a7b2-f6d8-341c-aeeb-4ddf345f4e3a | -5.90131 | -44.74799 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09ed57fe-4357-3dfe-ab13-aa865af69bad | -6.45079 | -43.88656 | 2025-10-17 04:19:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 485e4246-2e51-3a7f-8999-bb12718d122d | -6.23144 | -42.49738 | 2025-10-17 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3de4ba2c-feca-3c4a-8dc2-24bef59c0d10 | -5.01015 | -44.68052 | 2025-10-17 04:19:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 020cd1fc-e36e-3596-91ef-90648337b61f | -5.60958 | -42.68527 | 2025-10-17 04:19:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bb66bf97-20e1-3b9c-b61d-8d0d77c27e72 | -8.19987 | -43.96819 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce75e0c1-904c-33d7-9f93-035ee3d38c9e | -4.36982 | -48.71263 | 2025-10-17 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44ccb808-89ef-372d-b2a8-6306730f7138 | -6.3939 | -41.89711 | 2025-10-17 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b4d606c8-bd1e-3aff-93cb-3d98915bc0de | -9.26655 | -45.27378 | 2025-10-17 04:19:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4e5738a3-1a68-3a67-9404-21ed5faf7dc9 | -5.16441 | -45.21228 | 2025-10-17 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50df6938-8b84-3d46-af46-3c6ad5b51ef1 | -6.60808 | -42.06501 | 2025-10-17 04:19:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 71f9d0a5-a21c-35e8-8a49-4aad90083ecd | -5.43447 | -44.4025 | 2025-10-17 04:19:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f65f585-1a90-3c83-a14f-b75eb078e657 | -6.7379 | -44.16288 | 2025-10-17 04:19:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c5abcf9d-1d9d-3fb5-94d6-4027702784bb | -9.72489 | -48.91395 | 2025-10-17 04:19:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 524b1628-985a-3b3b-a802-66fdbebe410b | -6.29237 | -45.50569 | 2025-10-17 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3afdcd4a-6a7f-30ac-92bc-a202f788f916 | -5.31846 | -42.93763 | 2025-10-17 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 82ae3842-f558-3855-b9a8-dc257bffd8b9 | -10.27011 | -44.03408 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db060126-7464-3f1a-a406-c28c4ebc9633 | -7.75234 | -42.50061 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7140f881-2e9c-34fc-9fb2-5d0cc20f941d | -4.12596 | -42.2021 | 2025-10-17 04:19:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 618de8a0-7d2b-3c9a-a2e5-5c8c26008252 | -7.7188 | -47.84248 | 2025-10-17 04:19:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d5266a4-2bc6-3ee1-8d9b-dc7e90ad361f | -8.3036 | -43.42493 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c8d19e28-4269-34f1-b9bb-3d9e9babd0a8 | -8.24893 | -43.42032 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f6c9aed1-4f2f-3181-b5e0-30176a42686c | -10.61619 | -42.31538 | 2025-10-17 04:19:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 62b62efc-0f51-3240-a20e-d320df742c2d | -10.52849 | -43.36892 | 2025-10-17 04:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ad3e7915-4410-36bb-9ffa-7cd7ab408545 | -8.62131 | -54.56339 | 2025-10-17 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9fbf9d1c-4fe3-390a-8c0b-0d9b7ea80026 | -10.28077 | -44.03199 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 65f842d2-bdae-3d4b-9af0-e0eb5489d720 | -7.17838 | -42.52378 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4a3a8c06-f509-31a0-aa48-34a6cbdb4f75 | -5.48817 | -45.4033 | 2025-10-17 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cfe0d232-5a7d-36bf-ae86-fc80c05bf6fb | -6.74469 | -44.38021 | 2025-10-17 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d2c3150-15e5-31b9-9e60-6960b017f87e | -4.57448 | -48.02522 | 2025-10-17 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7fd956e-69de-3ff1-89ce-07b5dd793c55 | -5.62146 | -42.67587 | 2025-10-17 04:19:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d34d5b39-ca2a-3e66-b3eb-23c882a6e01c | -4.60583 | -50.91113 | 2025-10-17 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 932f2452-16bd-343c-8b89-12922d4a0a9a | -4.41154 | -48.94669 | 2025-10-17 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a07fa3ae-6138-3200-bda8-c6db278eb13e | -7.4835 | -38.99788 | 2025-10-17 04:19:00 | NOAA-21 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9f71dd31-1278-3a21-9e1e-1256a52a4296 | -10.66337 | -45.32298 | 2025-10-17 04:19:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa7deb02-9b19-3bf6-9041-25e158166f05 | -6.13812 | -41.72098 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 14c199b0-55c7-3b8d-bdc5-01165b17f95c | -4.89466 | -47.64057 | 2025-10-17 04:19:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9038e835-ddba-3365-b23c-9afbaf61b68f | -6.40299 | -41.50019 | 2025-10-17 04:19:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d0c45876-dc3b-345f-a23c-9417307ba3b1 | -6.63545 | -44.44793 | 2025-10-17 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 169a79ab-dbf3-37bb-92a6-265a7ccb2465 | -4.33979 | -43.80705 | 2025-10-17 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8a90fa9-a076-3b59-870f-49f1cc1558c8 | -6.20539 | -41.75426 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 6ee79369-02dc-37cc-a6be-8a13f21e8e4a | -11.06169 | -44.66094 | 2025-10-17 04:19:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 008f4742-9d96-3d64-8564-e683ba29d28c | -7.68002 | -44.62362 | 2025-10-17 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a6394bf-53a8-3641-a20e-fab5986bd876 | -3.28934 | -52.54445 | 2025-10-17 04:19:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e93f499-0833-374c-9c09-33218b8b2a6c | -6.31282 | -45.52684 | 2025-10-17 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05742ae5-4b62-353b-b33f-c3a97d10c9a4 | -6.15793 | -40.90917 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2eaaa179-e1da-3f42-80dd-f174425d39a4 | -7.68224 | -44.63105 | 2025-10-17 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2721b24f-d9df-31f8-aa64-ab9b25f9e42f | -6.53029 | -42.19323 | 2025-10-17 04:19:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0f97e39d-46b8-37ba-a979-9bdc1fc8d374 | -4.22158 | -48.36275 | 2025-10-17 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ffc318d-9806-397c-8854-2ce3c58c0cbe | -10.11576 | -44.62167 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7e77a058-4777-364b-bb67-fdb5b7331696 | -7.47063 | -41.5205 | 2025-10-17 04:19:00 | NOAA-21 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fa3e64b8-d385-3181-bae0-51dd4b218e27 | -10.12181 | -44.60454 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e01380f9-e034-3515-a991-5c02265fb976 | -8.3909 | -46.24655 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d48b4898-cc93-3d19-89b6-492a4a3e5043 | -4.42276 | -43.40583 | 2025-10-17 04:19:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 516ac9df-05a6-3504-b68a-f309807a28a0 | -2.88143 | -50.73978 | 2025-10-17 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee087159-ad9f-346b-8e01-d5920bff9ba0 | -7.28395 | -42.31055 | 2025-10-17 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 41c3a8cc-07b6-3cd5-bd60-7d0a77936f3d | -8.29858 | -43.45788 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fba9d98b-2357-37b2-a687-405018753c49 | -5.32685 | -42.92785 | 2025-10-17 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24d57046-14dd-3ff5-b5b8-ef1304b786a9 | -5.49666 | -43.80856 | 2025-10-17 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16f7482d-df52-3397-8163-6e81193a2899 | -7.34396 | -44.15847 | 2025-10-17 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f1a696e3-541c-33d6-8cbb-b35dcb6c95bc | -5.86575 | -47.58249 | 2025-10-17 04:19:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b04ee9d9-b8ec-3067-9e38-94c55c80a9cb | -7.46834 | -42.17089 | 2025-10-17 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 208d60e1-5be4-3ad1-80cd-5e4a09cfbfff | -10.92061 | -47.86103 | 2025-10-17 04:19:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e563f6a-52f9-3cee-ad2b-538e80c80bbc | -8.06721 | -45.41158 | 2025-10-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0ac94245-7b6b-3548-8d1b-ca4efd179287 | -7.90805 | -50.39052 | 2025-10-17 04:19:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| ad46d927-9fee-381e-ace0-dc39d64cc337 | -9.71503 | -44.55167 | 2025-10-17 04:19:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4fa7955d-6d1a-338a-a05e-4921914f6ddd | -10.83158 | -43.93948 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f39c3e0-c30d-3813-aa2c-04d2dab88e7f | -8.20153 | -43.31221 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| ea5ed3b6-8bf5-3a56-89c8-5d4049dff29d | -11.39084 | -44.21215 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54cee394-02b7-35f0-8c1e-bd7d08b0d18d | -6.40805 | -47.21507 | 2025-10-17 04:19:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 198b3ad3-82a8-39b5-b9a2-ab7c2bc183cf | -7.12008 | -44.72228 | 2025-10-17 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42d82cdc-c44f-3256-805a-1b30bcb02287 | -4.93356 | -41.54211 | 2025-10-17 04:19:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4e037b93-6086-3458-abda-7884756696ad | -6.39877 | -41.50378 | 2025-10-17 04:19:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fb6942d7-c286-3fa2-af33-d55af9c3a0e4 | -7.60737 | -46.88049 | 2025-10-17 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3817784f-a601-3819-8b25-9d8f9b2808a0 | -5.28434 | -47.92228 | 2025-10-17 04:19:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1552b51b-4336-3b2e-82c2-89763b269e8f | -10.92813 | -45.41556 | 2025-10-17 04:19:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc1aa56b-cd8b-3ebe-859b-f96212f20c73 | -9.88331 | -49.29408 | 2025-10-17 04:19:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ddeea941-b180-376d-8dd7-95fba00d03cb | -5.50399 | -47.30753 | 2025-10-17 04:19:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 37b6505c-02d5-3c92-94ba-e2efdbbb58c4 | -8.38619 | -46.31895 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 920ce93a-75a6-342a-8efe-4ca306107bb3 | -6.95876 | -47.71621 | 2025-10-17 04:19:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f202ca2-bdc7-331f-b789-89a05143fe7b | -9.18108 | -47.71229 | 2025-10-17 04:19:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 88b7742a-7bff-363b-bd63-c864f3397818 | -7.68353 | -42.56628 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ed64d373-7304-3e3b-8902-c680d07a7a96 | -6.40187 | -41.48307 | 2025-10-17 04:19:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c7e65162-7db1-3f65-86ae-cd1cabaeb47b | -6.20308 | -52.73786 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d53945f1-c2b0-3f10-8a61-7d2fbf889902 | -9.95959 | -43.86288 | 2025-10-17 04:19:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d05d90e-564f-3a53-811a-e8329f3f05e2 | -10.5096 | -43.42392 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3258aac5-ec83-3272-a74c-47096898c584 | -8.69925 | -46.97501 | 2025-10-17 04:19:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b31d44e-5059-3d5c-a26c-b810796fc5f9 | -5.34606 | -41.20846 | 2025-10-17 04:19:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README58.md)
