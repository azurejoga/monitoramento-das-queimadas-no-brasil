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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5db7c037-2288-3714-9aef-2cce6c34fdb1 | -3.80568 | -41.56794 | 2025-09-27 03:53:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| cbea2fc4-3816-3362-91f0-1b1f80979511 | -2.96441 | -48.59927 | 2025-09-27 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66ed54fc-11dc-332a-9f37-3415707ee8c9 | -6.18213 | -41.84502 | 2025-09-27 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 49f5c6eb-4592-3c09-9031-4893b477c882 | -3.96563 | -38.52132 | 2025-09-27 03:53:00 | NOAA-21 | ITAITINGA | CEARÁ | Brasil | 2306256 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a5c14ef0-c153-38ab-8735-0191c376242f | -5.73816 | -42.55647 | 2025-09-27 03:53:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 51130d92-d0b5-3884-aa64-62481c07cac1 | -4.38425 | -41.92263 | 2025-09-27 03:53:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c7833bf0-a509-3109-a8c7-17b36742377d | -6.26698 | -44.07539 | 2025-09-27 03:53:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 25deb5de-90ab-3ceb-aec3-c51ef09cc414 | -5.47934 | -43.07534 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 17b1f056-9fbc-3bf3-8880-091bcee228f1 | -4.57439 | -44.0697 | 2025-09-27 03:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| adf2be2e-d197-3c7e-b3ba-62e7e3c1a1ca | -3.50603 | -44.24874 | 2025-09-27 03:53:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec0292a5-f30e-3c77-97fd-195d2ce91f1c | -4.44764 | -40.97114 | 2025-09-27 03:53:00 | NOAA-21 | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bad2863b-98ce-3496-b0ad-3f4a519b13f8 | -3.87576 | -40.4458 | 2025-09-27 03:53:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 871aa216-2ac4-3995-9199-af7808928acc | -6.15936 | -43.99194 | 2025-09-27 03:53:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db9203fc-877a-3e92-be9d-cebedfc232a6 | -4.99452 | -47.35724 | 2025-09-27 03:53:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cafc403e-c9aa-3ea9-93be-b558e1fae0e1 | -4.388 | -41.92327 | 2025-09-27 03:53:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f35dd21f-c390-30b0-9b2e-5ef79ee6c165 | -5.71788 | -44.51826 | 2025-09-27 03:53:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e38bdc57-2b02-3ca0-9059-0ef3d478a5a1 | -5.76419 | -42.80905 | 2025-09-27 03:53:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 67fc92c8-eaf2-343e-aa36-2dd65c006cfb | -7.15041 | -35.79666 | 2025-09-27 03:53:00 | NOAA-21 | LAGOA SECA | PARAÍBA | Brasil | 2508307 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 63436200-5f0d-3b28-b1c8-7616ef36f32a | -6.12815 | -43.45638 | 2025-09-27 03:53:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7cf5d2ce-bb47-3c12-b995-740488eb0000 | -5.47593 | -43.07131 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| d1a9c4fc-cae5-327c-9cca-432482d466ba | -5.67424 | -44.85352 | 2025-09-27 03:53:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 523b4ba9-510f-3748-83a8-a0d5f9934e2b | -5.46457 | -43.06598 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6975c8eb-53a9-386c-9468-ae194548f79a | -5.46289 | -43.07619 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d54d2dd-8353-3bfb-a48d-8f36c5cc47e0 | -5.83695 | -43.91956 | 2025-09-27 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2441103e-0329-3b53-89e8-d357fb497fe5 | -5.43032 | -41.31765 | 2025-09-27 03:53:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 81b48d7e-b923-3f8d-8d82-603713e39704 | -5.51092 | -43.86794 | 2025-09-27 03:53:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5ba697a5-9e93-3394-a3bf-26b8328a1e2d | -5.31136 | -42.77214 | 2025-09-27 03:53:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2540c6c4-2fdb-3d51-8cfa-04112f194c51 | -5.50226 | -42.19474 | 2025-09-27 03:53:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 418dcdb5-1c0b-330a-9661-c5cebd8d63b5 | -5.45835 | -43.07902 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b63c182-7297-3c3c-89b7-4790610374b9 | -4.79474 | -43.1992 | 2025-09-27 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 095e0191-662c-39e8-b5e5-c31239acc660 | -5.7881 | -41.75173 | 2025-09-27 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 934d468a-c4c4-3c01-b9ba-19117639bfd9 | -3.23734 | -46.80276 | 2025-09-27 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 92ab80b9-536e-3813-bc0e-215480916ce7 | -6.11205 | -43.90644 | 2025-09-27 03:53:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0a32a11-51e7-3162-92b8-6924367d96db | -4.38497 | -41.91807 | 2025-09-27 03:53:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 17aa3cc4-94e2-376c-9b1f-4c1221d4699b | -3.58206 | -44.25643 | 2025-09-27 03:53:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d53ac0d-3acc-3712-8806-f58392995798 | -6.34506 | -43.7854 | 2025-09-27 03:53:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c988870-953f-36b4-9b39-2ef6aba2f973 | -4.48544 | -40.78341 | 2025-09-27 03:53:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3ec62d2a-4f4b-392a-8ec5-554487ba102e | -4.79812 | -45.12417 | 2025-09-27 03:53:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ba9268f-5983-3be0-8622-3d4af107e255 | -5.49013 | -43.08421 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 1f563fdc-1bb6-3a51-9710-7f05bb965bbb | -3.82518 | -40.35076 | 2025-09-27 03:53:00 | NOAA-21 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 75186986-1514-3685-b98c-456fda9c3219 | -5.25308 | -40.70839 | 2025-09-27 03:53:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b5f4ee39-11c4-33a0-9f0e-3503b0c33b7d | -6.62839 | -38.6853 | 2025-09-27 03:53:00 | NOAA-21 | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6c508cad-1bda-35ea-aca3-565f94a453fe | -6.24895 | -42.47647 | 2025-09-27 03:53:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7355f09f-383b-367c-afcb-7c3624749741 | -2.88186 | -40.4628 | 2025-09-27 03:53:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 71d68a98-af52-3c4a-ab76-f8541028f0a4 | -6.27598 | -44.07301 | 2025-09-27 03:53:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8393c380-d402-3e56-a3fc-874922bda46a | -5.74144 | -44.98704 | 2025-09-27 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 42b19905-6a22-3326-b96a-9762942270ba | -3.80197 | -41.56737 | 2025-09-27 03:53:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| ff4ea8fa-aa4d-338a-91fe-11dcf0f2a1fe | -5.36653 | -42.28847 | 2025-09-27 03:53:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 133e13e0-7e09-3fd0-8be1-f80d1fd597f4 | -2.95916 | -48.5938 | 2025-09-27 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 096aa7c9-f9d6-323a-b51e-c282199c285a | -5.47425 | -43.08158 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 15aa10d5-62ae-3dd0-a17d-946b96375d19 | -6.26598 | -42.49163 | 2025-09-27 03:53:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 39f4950b-e339-374f-b7d2-f36e7a3583a3 | -5.46346 | -43.07278 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4271ffbc-529f-3901-bfa3-b243fa1a1cc4 | -5.51254 | -43.88387 | 2025-09-27 03:53:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7eaf139-5247-34d8-8174-6b5114b121d4 | -4.70853 | -40.6332 | 2025-09-27 03:53:00 | NOAA-21 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a208fcf4-83df-300c-9a32-e96b3942739c | -3.30172 | -42.18025 | 2025-09-27 03:53:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 9504c698-7118-3730-82bc-7e59e7c71131 | -6.31427 | -43.38711 | 2025-09-27 03:53:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c1240f15-b06c-3f22-afb9-cbdc08ae93e9 | -5.08189 | -44.86129 | 2025-09-27 03:53:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b222c9cc-7c09-3f25-84a5-efd9a1b127c0 | -5.19752 | -37.36687 | 2025-09-27 03:53:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| decdccd5-4264-3e3f-9d70-0b9d0fa6175e | -4.80639 | -46.81319 | 2025-09-27 03:53:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 80cc8313-01d2-3b84-98c8-2d16dfa393a2 | -3.88052 | -40.43858 | 2025-09-27 03:53:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c9b1ad6f-5527-3aa6-9d53-5e1c15e56c53 | -5.76569 | -42.80652 | 2025-09-27 03:53:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 499aac51-2ab8-38f6-835e-74510ef588b1 | -5.79823 | -42.82685 | 2025-09-27 03:53:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ac477927-b1f0-3933-9d50-9e04e9c21d9a | -5.08409 | -44.848 | 2025-09-27 03:53:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 54d1ebf9-e81c-3f54-8ffe-fcbd5b6f7bd8 | -6.32037 | -43.4598 | 2025-09-27 03:53:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2ddcf1b-7710-3057-b091-9e7ea359ced4 | -6.40619 | -43.31535 | 2025-09-27 03:53:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b33d3347-d11c-3781-a6be-65c8f229e4ab | -3.74432 | -39.79905 | 2025-09-27 03:53:00 | NOAA-21 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 12927167-d2bc-3257-af38-6132d1df1cda | -6.13098 | -43.46417 | 2025-09-27 03:53:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf6d1a6a-a51d-3dad-b7ac-b0c455839e22 | -4.00382 | -46.96199 | 2025-09-27 03:53:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 969e2b12-b1d7-3d8b-ab68-cd04f499d21a | -6.32097 | -43.45628 | 2025-09-27 03:53:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 412e7a36-5ef0-3cb1-a832-e89c242e9a7c | -4.1483 | -39.99909 | 2025-09-27 03:53:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3601a500-3ca3-39dd-944d-cd9e2225dbd3 | -5.481 | -43.06521 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 009e3684-1054-3f0b-8289-d736e2e91c9d | -5.82507 | -41.29767 | 2025-09-27 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e62570d5-6dae-348b-b408-73e97df7f245 | -5.46799 | -43.07001 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 023901a4-924e-3173-a5fd-a2e48961e10b | -4.44051 | -40.97 | 2025-09-27 03:53:00 | NOAA-21 | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c2cbc7a5-c198-346f-85c7-c2c00d84f9cd | -3.82704 | -40.33912 | 2025-09-27 03:53:00 | NOAA-21 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d67d69c6-08d7-3a93-81fe-aa3725bfa1df | -5.07885 | -44.85173 | 2025-09-27 03:53:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 2d327245-3f71-3117-b388-b86dcdc00f6e | -5.5193 | -43.86919 | 2025-09-27 03:53:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 03f57683-f615-3731-a199-0587e93f8c60 | -3.80125 | -41.57178 | 2025-09-27 03:53:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| bb2270a1-313d-3588-b604-3a665625449a | -4.574 | -48.02193 | 2025-09-27 03:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b5b277a-7240-35e4-9580-c301d575eb65 | -5.12881 | -42.87828 | 2025-09-27 03:53:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33179611-de3d-3f63-8ba5-41bd81fc63fd | -4.45412 | -40.97626 | 2025-09-27 03:53:00 | NOAA-21 | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ca82e8b1-3921-3da2-8b85-770e193ca90f | -4.1672 | -44.26833 | 2025-09-27 03:53:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a215992-1383-3ec5-9be0-59daa5254dc8 | -3.96672 | -38.5144 | 2025-09-27 03:53:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 455ccde4-ce1a-3a09-855d-6a2e3bf89d32 | -6.1247 | -43.4523 | 2025-09-27 03:53:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e044c551-8bd5-352a-aa3f-2632b350d6ef | -5.50673 | -43.8673 | 2025-09-27 03:53:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c17e0fd-4028-3f4a-8620-87139b42af32 | -6.32157 | -43.45275 | 2025-09-27 03:53:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ea03a56b-d0b1-3d11-9f4d-203a496811b5 | -5.73775 | -44.98161 | 2025-09-27 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 24a71059-6fac-34b2-84d5-d311dd1dc74e | -5.48442 | -43.06921 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1140797c-de69-3f21-832b-40f05087e529 | -5.47196 | -43.07065 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| eb2d254f-2031-3ccc-b878-b9b24dc9c5c9 | -5.07673 | -41.18861 | 2025-09-27 03:53:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 68c828dd-b670-39ec-a0ac-c5654f9550ad | -4.00824 | -46.96338 | 2025-09-27 03:53:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cfc99bc5-2ba4-33f6-9ebc-c00b42a57af4 | -4.33514 | -48.39286 | 2025-09-27 03:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92ec04d2-69c9-3ba5-b429-36fc58728bf1 | -6.33485 | -43.36156 | 2025-09-27 03:53:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f080b947-2d7e-35cc-9bce-b0650144ab70 | -6.31827 | -43.38777 | 2025-09-27 03:53:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6a116278-cf98-358b-b7a0-1225a6510c9a | -5.60031 | -45.36928 | 2025-09-27 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5795f5f-f51e-3604-b316-4aa41796f314 | -6.42247 | -43.07095 | 2025-09-27 03:53:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 40b6cfc9-c8b3-36aa-9b91-fe2cb5a03730 | -5.14641 | -37.73829 | 2025-09-27 03:53:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 0a5e9ade-6a69-386c-8d1b-87e09d49ecad | -5.14577 | -42.6741 | 2025-09-27 03:53:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8fb400e5-7560-3096-b8d9-f42ded4efed1 | -5.73396 | -42.65351 | 2025-09-27 03:53:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 23f8beed-30d4-3546-a6e1-965790aa832a | -5.05971 | -40.82359 | 2025-09-27 03:53:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README13.md)
