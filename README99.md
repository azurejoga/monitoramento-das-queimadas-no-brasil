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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03301a66-9455-3f89-97ca-901ac8f6aa1f | -17.76409 | -57.3563 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 13957828-ba91-33ad-b922-00c54109068b | -17.76373 | -57.3595 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 437e1f31-307b-3005-98b3-680251c4d47b | -17.75893 | -57.35564 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 4bc5851c-5f4f-34a1-a8dc-058f02481364 | -17.75857 | -57.35885 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| bfd05dd5-7f6e-3d38-a9a2-83eae043bae5 | -17.74167 | -57.36972 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d66179a2-877a-3cf3-9a8b-8ee02d3120a8 | -17.2967 | -57.2993 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 7a265d24-9795-3916-90d5-e00042bd141d | -17.2912 | -57.30182 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| f93327b4-6491-3569-b509-4c049a12cce6 | -17.27252 | -57.26423 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 8ba0d11f-86dc-3779-9ecd-408f7a427fe2 | -17.26924 | -57.2633 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c872da92-7e48-333b-ab2d-6f59f3ec0c84 | -17.26736 | -57.26357 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| fd5f8064-478a-3b44-a220-b3aaafda6bfc | -17.932 | -57.53157 | 2024-10-26 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| a8ecef4c-8ede-3287-861c-8b5f33dfc630 | -17.26699 | -57.26677 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 5e042bbd-ebe5-37cc-b84d-221c986447c7 | -17.26293 | -57.25651 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 335cb118-84bc-3575-a9da-14fd0db6d2b9 | -17.26256 | -57.25971 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9e704d30-45a6-3bc6-88b1-432f42a8e8cb | -17.2622 | -57.26291 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 01954ff3-4dd1-35d1-9695-b672009bbbbf | -17.26183 | -57.2661 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 663ffef8-0504-3ac2-9acc-e7f72b33d168 | -17.23881 | -57.1914 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 877a0c8b-256b-34a6-902c-df0b129ea0a7 | -17.23845 | -57.19463 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 795fc691-c2bc-3bd4-890f-8c08c79f1fd9 | -17.23809 | -57.19786 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| b2791dee-f134-31aa-8a1c-787be1a555e8 | -17.23291 | -57.19721 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| f8b44080-30c1-3ffc-a05b-98c168bf0cb9 | -17.23255 | -57.20043 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| eb590e2d-c5f1-3196-9b08-cfc76930f9ac | -17.23219 | -57.20365 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| fa95bff3-f513-3409-a5f6-cfdd610cd4e9 | -17.22701 | -57.203 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 6bcb2e08-55a2-3927-9cff-d4a8a73e270e | -17.22665 | -57.20621 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9bb2405f-0ab7-34c7-a07f-3a624e4efd8a | -17.22558 | -57.21588 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| ac0a49a0-d800-3e6e-84ce-69e921c70ce9 | -17.22522 | -57.2191 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 83768153-a7f9-376f-9377-b33978215665 | -17.21969 | -57.22165 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 2afc8973-7b58-3cbe-b70c-d66ae77df4c5 | -17.21933 | -57.22488 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 3d3d4ac6-5227-35eb-b762-cea47beb2b7a | -17.21898 | -57.22809 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 7986d3fe-5411-3c7f-9d42-024eba5d0ecf | -17.21862 | -57.23131 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 707f4258-d504-3ace-810f-4db7f0f64f62 | -17.21062 | -57.25626 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 0decc5e4-cd53-33cd-8bcd-e009544676a7 | -17.21026 | -57.25946 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 1d24836a-cb35-367f-bb18-abf6cdda90bc | -17.20404 | -57.26839 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| fddf9f6e-8d62-3f27-99b7-3207fba2d203 | -17.20369 | -57.27158 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 1cf2eda6-31df-390e-9d12-1ad441220393 | -17.20334 | -57.27478 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 32ae9024-5922-33c2-ac9d-a97d01f8eb45 | -17.20298 | -57.27797 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e347e975-88d6-3e94-a04e-1e82897b52cd | -17.19163 | -57.28619 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 998f5527-6992-3339-9d86-41cfee0231f7 | -17.19128 | -57.28938 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 304cec00-e41f-3771-8e65-238bc54cd6a5 | -17.18648 | -57.28552 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 32749f8b-ca51-3ef9-82ec-8888eaebc8bd | -16.88817 | -57.27664 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a8bdbd5c-28e5-3fae-b1cc-147ca5730caf | -16.88781 | -57.27981 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 1afd0bfa-ddd8-3828-a957-3da8050a8e42 | -16.74791 | -56.66691 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b8b790bc-49e5-3f07-8a90-47319b8c8730 | -16.74753 | -56.67036 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 37b04426-be96-3d8a-a125-40ef7f28961b | -17.79724 | -57.341 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 85cbcef0-c1b3-3f5a-a8dd-3aafbc70e1a3 | -17.79688 | -57.34421 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| dca83507-a10a-345d-b3d7-3619f02a1a1e | -17.79505 | -57.36027 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| ae632046-eecf-3731-a9bc-3b86712afdd2 | -17.79469 | -57.36347 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| eefda997-a618-36d9-9ce4-f90a2c135ba3 | -17.79374 | -57.34271 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| ccaf2557-e172-3278-8797-17b64803abf5 | -17.79169 | -57.36202 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d5857971-1f56-3638-a0e1-f871bcabb08b | -17.79101 | -57.36843 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 4fa9efdc-b234-36d4-8cc1-61ae2ea5e1a4 | -17.79025 | -57.3564 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| efe42f33-4a89-3fe7-aba8-5b8eb7932039 | -17.78763 | -57.33322 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.4 |
| db249b2b-e06c-37a7-8c9c-cd3854937f2a | -17.78174 | -57.339 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| e853722c-552f-3bd8-a5cd-675ce29802da | -17.77921 | -57.36148 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| f1ecc0b6-95dc-3afc-9b4c-2e85b232d548 | -17.77885 | -57.3647 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 5e62ee7a-d8e8-30a5-87d7-75917534f076 | -17.75821 | -57.36206 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| da1189e6-9159-3dc3-8193-b7f9105db697 | -17.75678 | -57.37489 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| b0071e09-1bf1-310b-bfca-948b234cae1b | -17.75643 | -57.3781 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 65a09a9a-169d-3802-85c5-5a89e3133da0 | -17.17773 | -57.41225 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e2d4424e-d2c8-3985-99b8-93dd009a4a7d | -17.07644 | -57.40932 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d95b274a-4435-3629-b8b7-c7e6beec266b | -17.07609 | -57.41243 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 7fd2aa74-88f2-33f6-8a93-f754362edb4b | -17.07169 | -57.40556 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6b3ffe98-755f-3764-b4c9-5131f466553b | -17.071 | -57.41177 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 6454bdf4-6c9d-30cc-93c6-02a269611a8c | -17.06962 | -57.42421 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2626afac-529c-3b1a-91a0-a1664e9a59f4 | -17.06927 | -57.42731 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 1cb980c4-f2a5-35b0-89d0-0610cd6db496 | -17.05708 | -57.39732 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 2cd255a1-40fe-3109-80de-7e89f5b08bf7 | -17.05602 | -57.45382 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 91eb1f67-7ecc-3c78-9949-dfc4694f387a | -17.05567 | -57.45692 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 0df8217d-d828-3d99-b54d-3933fcf1d00c | -17.05444 | -57.39258 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 7d9b1809-8046-39eb-b687-63948bdc2c47 | -17.05407 | -57.3957 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 4d6f03a2-4ca5-309c-b9ee-890da5d6e7c8 | -17.05371 | -57.39881 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| dc46bc74-5787-346d-a8e2-4784219a84e3 | -17.05297 | -57.43462 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 858744dd-bb2a-3825-b6aa-9d655969eeb9 | -17.05232 | -57.39352 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 350b8ed7-5882-3a91-8dbb-9d6469afbaae | -17.05198 | -57.39664 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 4ba5a15d-88c9-3fe7-b459-85328aef9f66 | -17.05163 | -57.39976 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 40666b5d-b723-3212-b843-3973506e49a0 | -17.05094 | -57.45316 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 5897ef1d-f3a9-3374-b411-7db209bc3e5f | -17.05008 | -57.42982 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5bce06a6-4b0c-310a-a483-75ce69363477 | -17.04935 | -57.43602 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| bb7c656c-26ba-3a06-a33f-86be5cad430c | -17.04898 | -57.43911 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 82bc616c-9c35-3d90-a6d3-841654f641dc | -17.04897 | -57.39504 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 013e7307-482a-3e54-a626-aa1f4fe72c00 | -17.04861 | -57.39815 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 8db5e58a-c559-3ec8-877a-ab7afd608853 | -17.04857 | -57.42773 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e67c3c60-86ac-3434-8932-09dc5be77c56 | -17.04823 | -57.43083 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 11fda010-0c8b-32b8-8344-18ae1a9a8b5b | -17.0479 | -57.44837 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e4583bc9-ea04-37bd-a2df-a9a120a9249e | -17.04755 | -57.43703 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 48f008af-3a48-3f90-86ff-fca85df94ce6 | -17.04753 | -57.45146 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 184f86de-2e01-3b1f-8a3d-284821320738 | -17.04688 | -57.39597 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| f5d47554-eab4-399b-98da-31dac0a707ab | -17.04499 | -57.42916 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 888a7dae-676b-31a7-aa6c-59e1b55ab9c1 | -17.0439 | -57.43844 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| f54a37d6-5eee-3704-ab24-42251334c614 | -17.04351 | -57.39751 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 4aa3a6ac-f52c-390a-9298-74327da7b613 | -16.9927 | -57.34337 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| cf981fb1-1948-3f93-80bd-be728fbad6c9 | -16.99235 | -57.34652 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b3ef78c0-75ec-37ab-8c27-57084a8b15f9 | -16.98814 | -57.384 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f6be4099-ced5-3fcf-ab3a-129283cce32f | -16.71109 | -57.45414 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 8c3706f9-6680-3948-82ff-e9264d62d761 | -16.70675 | -57.44739 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 71061025-2ac3-3d23-b0e2-c21a5b1a5de3 | -16.70639 | -57.45044 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c335ca67-3193-3bb4-a53e-1aa2c6758122 | -16.70603 | -57.45349 | 2024-10-26 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 39d5196a-f41c-33df-b10c-06d43020235f | -17.78124 | -57.50896 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| c8d1c6d5-9200-315c-a514-93e595c76e9b | -17.7809 | -57.51211 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| f31c303e-3fc9-3aec-b4d1-ed46933348d9 | -17.76449 | -57.49174 | 2024-10-26 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |


[Clique aqui para ver as próximas entradas](README100.md)
