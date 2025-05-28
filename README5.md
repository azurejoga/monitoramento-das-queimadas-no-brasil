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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7568647e-4446-3147-bfef-3137ad3f0cf8 | -12.41226 | -50.00167 | 2025-05-28 03:45:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9f75e927-aba6-3fdb-9c21-d3a5395531a1 | -11.39274 | -44.83145 | 2025-05-28 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 49863c77-99c9-3c0b-9431-d0b36a9e2d07 | -12.40838 | -49.99523 | 2025-05-28 03:45:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c09206eb-b3ff-3249-b581-f4e5131992d3 | -15.8038 | -43.57127 | 2025-05-28 03:45:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d25f1096-83f4-36b7-adb4-a9daa22c44b7 | -10.45579 | -47.94437 | 2025-05-28 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2fbc5228-ad15-3e64-9877-19a1910b95ff | -11.39201 | -44.83276 | 2025-05-28 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2c1fa110-6afe-34eb-87fc-8cc55a7bbab3 | -9.19836 | -49.47717 | 2025-05-28 03:45:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 4d3161fa-fb49-3461-be8c-e363823503ad | -16.75014 | -42.4738 | 2025-05-28 03:45:00 | NOAA-21 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53976dfd-7f8f-39f1-8c31-1ac45e2c59d8 | -11.81475 | -44.27346 | 2025-05-28 03:45:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 34.1 |
| a7b767fa-58e9-3a74-b80c-d6ad5e91cac8 | -10.65864 | -44.41171 | 2025-05-28 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2fd22fbe-80e1-3af7-9ddc-8297bb7b18fc | -12.27299 | -44.60171 | 2025-05-28 03:45:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63458fe4-454b-36d2-a70e-14064ca5aa58 | -12.45994 | -44.28472 | 2025-05-28 03:45:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 205ef894-773e-330c-a62c-c82fc1d928f3 | -9.15692 | -49.65142 | 2025-05-28 03:45:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7eae977f-fb1e-359c-83f7-adc0841fe788 | -13.08267 | -45.27639 | 2025-05-28 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2fcd775a-353e-37c7-a446-b5cc6676b7b1 | -11.82535 | -44.2699 | 2025-05-28 03:45:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c6206626-c1d4-3d03-b2ff-807cb1e1eedb | -11.82434 | -44.27523 | 2025-05-28 03:45:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e2fe6da9-2f25-3105-bee9-fe90209f4e94 | -12.4138 | -50.00292 | 2025-05-28 03:45:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b834139-057b-3d6c-a56f-0fbf3baaedd2 | -13.09269 | -45.27833 | 2025-05-28 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| baca5139-3948-39e9-af9f-5f2633b0ac55 | -11.39776 | -44.83231 | 2025-05-28 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 97c62423-e2b0-3da6-ac61-c7831d432076 | -11.82019 | -44.27266 | 2025-05-28 03:45:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 9e5bb2eb-8044-3b3b-a189-4430b56a30c8 | -11.39759 | -44.83067 | 2025-05-28 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| aaa31dfd-ceff-3b1c-99d6-acc9197bbb24 | -10.94954 | -48.15087 | 2025-05-28 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ebd7c405-f570-3b7b-a4e8-99862c95c5e0 | -12.27196 | -44.60729 | 2025-05-28 03:45:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c35e386d-3523-39d9-af97-a9f68342a2d7 | -11.40278 | -44.83324 | 2025-05-28 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| cc667e56-b50b-3f94-b56d-866a97c111df | -9.03774 | -47.74429 | 2025-05-28 03:45:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 9fd37f4b-c947-3e0f-96db-4b0f14339368 | -12.407 | -50.00166 | 2025-05-28 03:45:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f66827fc-32b6-36bf-800b-aea0640589b1 | -10.73243 | -49.29319 | 2025-05-28 03:45:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cdc039fd-ca36-373b-afc1-0d8eb3edeb3c | -11.81922 | -44.27802 | 2025-05-28 03:45:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 9ffe3d24-a88a-3b5d-8c2f-fc0b89b895e3 | -11.82116 | -44.26733 | 2025-05-28 03:45:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 23.1 |
| d8691b73-54b1-3eec-9a76-267a320b6323 | -10.4568 | -47.94773 | 2025-05-28 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 40c94931-65c4-3926-9e74-1d5df20556ff | -14.68683 | -45.09172 | 2025-05-28 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 496b6f47-6f93-313c-9c4b-f77129193cbf | -11.81373 | -44.27879 | 2025-05-28 03:45:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 44a87678-4110-301b-a6c0-a157db92e65b | -16.04595 | -43.80074 | 2025-05-28 03:45:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3965cfd9-8e46-39ab-8ac7-7a37a3caae1d | -10.75639 | -37.43869 | 2025-05-28 03:45:00 | NOAA-21 | ITABAIANA | SERGIPE | Brasil | 2802908 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fe22058f-1f68-3031-8fed-848a427fad4e | -9.89839 | -44.80324 | 2025-05-28 03:45:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27ebea6f-3cbd-35bc-8a7f-b2c949885090 | -11.82498 | -44.27357 | 2025-05-28 03:45:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 080ed0af-d5c1-3cfc-8537-4c1cd40306fe | -13.08768 | -45.27737 | 2025-05-28 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47b0e45a-d9fd-3c98-8b12-236d0e625d1d | -11.40331 | -44.83031 | 2025-05-28 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e7ab63b2-8d24-3038-b83e-7328fc9b7334 | -8.72678 | -47.99142 | 2025-05-28 03:45:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3b2060f0-5289-3350-b244-91c64357902b | -11.82056 | -44.269 | 2025-05-28 03:45:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 8a9a3a9e-a510-33ab-a5a1-575b1866c5b5 | -11.39704 | -44.8336 | 2025-05-28 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e0513b6c-d3f4-32c7-a52b-5b60cc438d7e | -10.47023 | -47.94496 | 2025-05-28 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f31c895c-83dd-38d2-ba2d-73b15a7ec8d0 | -12.28846 | -43.54328 | 2025-05-28 03:45:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f29d5c6f-ddb3-31a6-bf0a-ca09c257b373 | -11.8174 | -46.14402 | 2025-05-28 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f1d47fa3-6413-3d9f-bd30-174c9c0fd8ff | -11.57372 | -47.62552 | 2025-05-28 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1152237a-7079-333f-81ca-3a571e18ea3e | -14.68583 | -45.09699 | 2025-05-28 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9954a131-beca-32fa-afe5-2d7a276f5b48 | -11.56172 | -47.62344 | 2025-05-28 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4cc2b77-0d4e-35ff-a6e7-62760edcb925 | -16.6802 | -43.8844 | 2025-05-28 03:45:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13a3f259-697b-3c23-9197-f63302b7a103 | -9.03241 | -47.73819 | 2025-05-28 03:45:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 615ad573-5355-3031-af33-a22ec4a66885 | -11.81442 | -44.27712 | 2025-05-28 03:45:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 953f93bd-9cbc-3baf-9876-0e3dd010837a | -15.79954 | -43.57045 | 2025-05-28 03:45:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fbf22797-075a-358d-ab63-f4e32ae31acb | -12.28705 | -43.54514 | 2025-05-28 03:45:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1f3e8df6-d502-327e-87d6-9eecc82e8ad4 | -15.52587 | -42.64505 | 2025-05-28 03:45:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fc149296-850d-34da-abb5-2e62a23f6d9d | -10.47442 | -47.94794 | 2025-05-28 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c4631086-2568-3883-8dbe-53cbe2522b98 | -12.28758 | -43.54796 | 2025-05-28 03:45:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 92f03fb6-95e7-32b0-8c72-f1bf6d63d191 | -11.39815 | -44.82775 | 2025-05-28 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d5682bfc-8b26-3655-8e10-7a115a82f891 | -11.81809 | -46.14048 | 2025-05-28 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8535a61c-b739-3ef0-9d59-9b203e080710 | -11.39257 | -44.82982 | 2025-05-28 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a6eb4375-ead5-3b36-8f8f-ff947acf193a | -11.56773 | -47.62444 | 2025-05-28 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f4f72a28-6e18-3f43-9a71-457d09001198 | -9.03678 | -47.74925 | 2025-05-28 03:45:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2f2a20ec-73ea-3072-af21-7ab0db8ec967 | -11.40317 | -44.82867 | 2025-05-28 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 45286c2d-23e9-3a7a-92fa-aa79a67cba8d | -10.98613 | -44.62543 | 2025-05-28 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f59e2d3-275d-37dd-bf02-53e4b1b67ead | -13.09326 | -45.27537 | 2025-05-28 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c0f1a90-9a32-30c5-baf9-c45ffc5e34a4 | -10.52812 | -47.58462 | 2025-05-28 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d3edf543-6bfd-3aaa-bca3-368d1754446e | -11.81539 | -44.27178 | 2025-05-28 03:45:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 23.1 |
| e2bc6d85-7526-3c65-94ee-b85aaf226b60 | -16.04165 | -43.79986 | 2025-05-28 03:45:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a8c30017-e51f-3fc2-aa0d-0fab358ac5dc | -16.60944 | -43.32573 | 2025-05-28 03:45:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07338bea-a948-32ef-8e28-dc02b343ca19 | -10.67014 | -49.4482 | 2025-05-28 03:45:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b5bd939e-4db9-358b-b155-6c25afbc8462 | -9.19738 | -49.47766 | 2025-05-28 03:45:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 998c925a-5fe1-335d-8f0d-be3406134998 | -10.95457 | -48.14659 | 2025-05-28 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d57182ce-48cf-3fe8-8868-1243f27e2e36 | -11.3983 | -44.82938 | 2025-05-28 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| cae19197-77d6-38de-96a9-057251711408 | -10.65667 | -49.4453 | 2025-05-28 03:45:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1df049ec-9af3-322c-9d72-89a7f79cc315 | -9.19869 | -49.47118 | 2025-05-28 03:45:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c04e9724-e70b-3065-9579-a5e7449bbf82 | -15.51883 | -41.97265 | 2025-05-28 03:45:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d95516cc-b871-3032-af5f-2457f319a787 | -16.7492 | -42.47897 | 2025-05-28 03:45:00 | NOAA-21 | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2eb54b47-68ef-361d-a17b-5d3aef6bb8c8 | -15.80458 | -43.56712 | 2025-05-28 03:45:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 309a3d97-164b-3e6a-aa8a-e2638bc178c4 | -10.73373 | -49.28689 | 2025-05-28 03:45:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e7e4a055-18c9-3c28-9760-cfbee5f4cf60 | -20.60783 | -47.22452 | 2025-05-28 03:47:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f302b132-5dc3-375d-bddc-cb333ccbd838 | -22.69967 | -43.3481 | 2025-05-28 03:47:00 | NOAA-21 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fb62f4b2-63f2-3238-b386-a8b2e10ea962 | -19.43674 | -44.34044 | 2025-05-28 03:47:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b8194d55-a496-3f22-a723-3b24404a1b36 | -17.78083 | -42.80985 | 2025-05-28 03:47:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cbe31e55-6470-3a80-9007-aea5ffef9d73 | -17.67558 | -42.74388 | 2025-05-28 03:47:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77107063-470e-3a22-ab52-ea4500035597 | -17.28372 | -42.65291 | 2025-05-28 03:47:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 57803149-5fe7-3974-867a-629066c3c0b7 | -20.34889 | -40.36185 | 2025-05-28 03:47:00 | NOAA-21 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2f527f04-f9d6-3422-8e3d-c4a0f97f1485 | -17.59496 | -43.19926 | 2025-05-28 03:47:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9a1a88d3-083f-3c0a-ad3e-0bd6b6972fe1 | -17.27584 | -42.65155 | 2025-05-28 03:47:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 45afab75-00de-3f7b-8ffa-165e61dfe2d7 | -17.95349 | -44.41981 | 2025-05-28 03:47:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 980549d8-4d0f-3d3e-9345-7aceb01e18ed | -17.67557 | -42.74643 | 2025-05-28 03:47:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec0bab7e-8dd9-36f7-9bae-3ff9bfd94187 | -17.09627 | -43.80386 | 2025-05-28 03:47:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0bea907e-8703-341d-9450-6a05a2fd9ae7 | -22.17759 | -42.47029 | 2025-05-28 03:47:00 | NOAA-21 | BOM JARDIM | RIO DE JANEIRO | Brasil | 3300506 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0056c86f-e504-391e-bf53-fd9db8184c68 | -22.78825 | -43.7555 | 2025-05-28 03:47:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6beee59b-f33b-31df-8cff-8087707f16a1 | -17.95264 | -44.42425 | 2025-05-28 03:47:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bf0bacdb-dbf8-38a4-8a25-382c6fc22530 | -17.27978 | -42.65222 | 2025-05-28 03:47:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 03202eda-e382-30d4-abf9-03995f6e7417 | -22.7711 | -43.27703 | 2025-05-28 03:47:00 | NOAA-21 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2f7041e3-718e-378a-95d8-c9698cbf9a84 | -20.60872 | -47.22608 | 2025-05-28 03:47:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e25c0eb5-d393-3f88-9317-a73b393cf615 | -20.61272 | -47.22575 | 2025-05-28 03:47:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b151deae-ca91-30b5-a8fc-adb62c0f9090 | -11.818 | -44.2703 | 2025-05-28 03:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 5be8af8b-bc1e-344b-aba4-e9a5ef57e5dd | -7.6762 | -46.0995 | 2025-05-28 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 8c90abf1-eaed-357d-ab15-7737006530be | -7.6762 | -46.0995 | 2025-05-28 04:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 847c55a6-5855-3fa4-95a0-bd846d5d899a | -11.818 | -44.2703 | 2025-05-28 04:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |


[Clique aqui para ver as próximas entradas](README6.md)
