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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fac45831-7aa9-3c7e-97f6-1f350a03136c | -6.67809 | -43.49913 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a353aac8-78fc-35ac-9d7b-5861c0942583 | -6.51071 | -43.15197 | 2024-10-02 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8946f4da-cf20-37c9-b7ed-9bebd73f4914 | -6.50583 | -43.15119 | 2024-10-02 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8332cad7-e3a2-3a1c-8a26-d766e981ec94 | -6.50247 | -43.15466 | 2024-10-02 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6215ea01-26dd-3ed1-8c37-68443cccc9fc | -6.49759 | -43.1539 | 2024-10-02 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 58656535-2047-3cb8-92bd-00542c06b6d6 | -6.47004 | -43.48181 | 2024-10-02 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a3954fb0-72e0-3279-9e5d-a857c1daba30 | -8.50744 | -43.92126 | 2024-10-02 04:46:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 29fafeb7-a702-34cf-8614-317c440eb25f | -8.50267 | -43.92054 | 2024-10-02 04:46:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| cd587ad0-37a7-3c14-93f0-bb1b70a876a8 | -8.18092 | -43.66153 | 2024-10-02 04:46:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43674bb1-e13e-39ed-a123-f842cc6d6ca7 | -8.17961 | -43.67759 | 2024-10-02 04:46:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e6cc9a24-67bc-3c43-9f29-278a48943372 | -8.17873 | -43.6779 | 2024-10-02 04:46:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f1384a1-9233-33bc-a981-eaa34aea5f3d | -8.17801 | -43.68331 | 2024-10-02 04:46:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d353b88-922a-350f-9b49-d6dc7d6b2201 | -8.17708 | -43.6607 | 2024-10-02 04:46:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3d44ea8a-817a-3af5-9bf4-5be15bb6b098 | -8.17402 | -43.68225 | 2024-10-02 04:46:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4231e560-f83c-3b21-958b-36097411c2fd | -8.16845 | -43.68682 | 2024-10-02 04:46:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b2d76027-ca4b-3a6b-af0c-730eef0d885a | -8.1677 | -43.69212 | 2024-10-02 04:46:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ca16851b-bb61-3cdb-b816-1f33d327461a | -8.16765 | -43.68711 | 2024-10-02 04:46:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 937e7a4b-bd35-373b-8249-bcf62e6d0843 | -8.16659 | -43.66506 | 2024-10-02 04:46:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cd82b3c0-8f84-3941-ae50-da8146bb3c43 | -8.16563 | -43.66534 | 2024-10-02 04:46:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c079e586-bc47-32d5-8990-5af85fc22a15 | -8.16362 | -43.68614 | 2024-10-02 04:46:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 08af116f-5aeb-32d0-9b32-47bfc5307ebb | -12.44181 | -43.72611 | 2024-10-02 04:46:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7e524cae-7695-34c4-87fa-3698a0586f7f | -12.44142 | -43.72918 | 2024-10-02 04:46:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 4d1d737e-8ba8-3c11-914d-dd61f5faf686 | -12.44102 | -43.73227 | 2024-10-02 04:46:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 4cfc2faa-4d46-33e0-9ac8-7dc26571f9ed | -5.40502 | -43.43973 | 2024-10-02 04:46:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2aa42a75-4741-3343-944e-f68bbb43cbe0 | -5.40317 | -43.43863 | 2024-10-02 04:46:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f6e02cef-1262-3046-8ab1-d5cf2e58d49f | -5.40032 | -43.43891 | 2024-10-02 04:46:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 206aa04a-f68d-3162-8cb9-dc00c041baea | -5.71354 | -43.94164 | 2024-10-02 04:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49f0a519-d501-330c-ab55-b51c269172b4 | -5.71029 | -43.93182 | 2024-10-02 04:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6cda27aa-9f84-3ac5-82a4-f4f5e6ae75ab | -5.70963 | -43.93639 | 2024-10-02 04:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf8c1475-65f0-3796-ae12-9cc9062400c3 | -5.70897 | -43.94094 | 2024-10-02 04:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2856bce5-cbdc-3e08-a64f-d8dc97a4ec0e | -5.62653 | -43.63342 | 2024-10-02 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eac9dfe0-0f7f-3a08-a6cb-09b6f199cfe9 | -9.12572 | -45.17042 | 2024-10-02 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7be5d7d8-3bdd-32bc-ab9d-e1bb30d23bfc | -6.10302 | -44.03851 | 2024-10-02 04:46:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1efd2bf3-0319-3f7a-89ee-53ab36dfac2e | -6.09907 | -44.03348 | 2024-10-02 04:46:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd01ea27-a6ec-31c3-bdbe-a5a4080de433 | -6.09846 | -44.03778 | 2024-10-02 04:46:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52e4560a-56b9-3118-9661-ee47273964fa | -5.8218 | -44.13103 | 2024-10-02 04:46:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f30584c-63e7-307a-8b4a-d6e5d2b82ae0 | -5.68713 | -44.18712 | 2024-10-02 04:46:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf6ec40c-5465-3736-a945-dee35599a644 | -5.68264 | -44.1864 | 2024-10-02 04:46:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f08e624b-b0ea-3d0d-ab98-afa334e967d6 | -5.68198 | -44.19096 | 2024-10-02 04:46:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2dc6838-c921-3d84-80a5-7d31ac726524 | -5.56983 | -44.09377 | 2024-10-02 04:46:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de01a6e4-19eb-35d2-8416-1f9591654620 | -6.70637 | -44.53996 | 2024-10-02 04:46:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f44c51ae-8e33-3f96-9e39-60c0eb5b6637 | -6.69771 | -44.69423 | 2024-10-02 04:46:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77f71dc2-40df-3161-b79a-bcde03e69200 | -6.66085 | -44.9788 | 2024-10-02 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b613a8e-6aa0-3c31-9831-bc53592fa585 | -6.61918 | -44.20126 | 2024-10-02 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b63dd93-9cb3-3435-93ec-e17887f1b31c | -6.61866 | -44.27042 | 2024-10-02 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e17e3c3e-1a33-3b03-bdf1-ea56a8cac3c4 | -6.61851 | -44.20599 | 2024-10-02 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37982c98-4f12-3098-acc9-c903446471cf | -6.59912 | -44.17847 | 2024-10-02 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 74ac8571-04e5-3065-9d60-85252bb7fdf8 | -6.59844 | -44.18336 | 2024-10-02 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9959d171-aa1c-374b-b173-34f741028060 | -6.59771 | -44.18171 | 2024-10-02 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 525d77b9-33a6-3475-99f5-df96ec3983cf | -6.59477 | -44.62893 | 2024-10-02 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1fcfbbd5-03c8-376c-bd4e-066d7ff83a72 | -6.58848 | -44.64123 | 2024-10-02 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ddc5b09-fdc6-3b69-b10b-d9dcdd1df8df | -7.69873 | -44.92838 | 2024-10-02 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 62de0d6f-ab17-318b-9ef7-6237b4483cd6 | -7.58959 | -45.28143 | 2024-10-02 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 78864a3c-aedc-3576-8465-694aee194528 | -7.58414 | -45.28889 | 2024-10-02 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8f4f8778-9a21-3b5d-8cdf-1b6557106558 | -7.57989 | -45.288 | 2024-10-02 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2c485372-c259-35a6-9684-0bc2dba5c817 | -7.57476 | -45.01251 | 2024-10-02 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d9229b1a-897b-3650-aada-2ffa678bc325 | -7.57038 | -45.01198 | 2024-10-02 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4cd14a41-cacb-30a6-90df-18a814d0bcfc | -7.40546 | -45.18185 | 2024-10-02 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0d94f2da-b57f-3369-aadf-fbfe354ccdc9 | -7.23321 | -45.00254 | 2024-10-02 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c0eb6749-265b-398e-ad47-06452ba76d0c | -7.23036 | -45.00096 | 2024-10-02 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9030c3ad-4ff7-3919-b95e-0e7d7db8b090 | -6.93973 | -44.44942 | 2024-10-02 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 06ed7a28-0775-3b75-92b8-2c6d66b8b072 | -9.13015 | -45.17102 | 2024-10-02 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68549337-d1f2-33cf-8379-24990c0c7133 | -9.0202 | -45.21662 | 2024-10-02 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 26cf7c2c-b055-36f4-85c8-e787a8dc6553 | -9.01954 | -45.22126 | 2024-10-02 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9eb1bedc-eb4b-38b6-b7b2-2d29ed32421a | -9.01393 | -45.22923 | 2024-10-02 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5836b2b1-9468-35c5-9f22-7f568625f07c | -8.99889 | -45.24051 | 2024-10-02 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 788fab3a-0f00-3162-8988-da2836a28265 | -8.99827 | -45.24492 | 2024-10-02 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b528c121-bd43-3a65-a5cb-817815925b54 | -8.89869 | -44.10021 | 2024-10-02 04:46:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 933f35f1-5c1a-3cf7-a5ef-35fbe6c12b80 | -8.89461 | -44.09456 | 2024-10-02 04:46:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1eb64322-5f7d-3fc3-8ce2-a15d0dc7300a | -8.89393 | -44.09959 | 2024-10-02 04:46:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eb423fc0-ee4b-35b4-8878-c58510ecaab8 | -8.87085 | -45.06282 | 2024-10-02 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 45c310b4-e44a-3636-8adc-48a718ab6da7 | -8.71578 | -45.21025 | 2024-10-02 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c92de48d-d297-36e3-8835-bb0f4cd4bae5 | -8.71347 | -45.22717 | 2024-10-02 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ca1b722-0b0e-3da9-a206-ab55d3f27783 | -8.71312 | -45.22515 | 2024-10-02 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f82473bf-f840-3337-b7e7-8153dcf45c3e | -8.71253 | -45.22929 | 2024-10-02 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70eaf9b5-250b-3085-ada6-78c6a21f280a | -8.7108 | -45.21402 | 2024-10-02 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77688bb9-b2a1-3bce-a882-73119746163d | -8.70964 | -45.22252 | 2024-10-02 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8018d29-4900-3155-a8b1-9ae12b4e4167 | -8.70873 | -45.22463 | 2024-10-02 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5fda625d-042a-38c8-af32-574ae4ae5ed3 | -8.70852 | -45.23079 | 2024-10-02 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea934504-017b-3e6e-bf6c-56cd225ccff3 | -8.70356 | -45.23441 | 2024-10-02 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ce3fd62-55ee-3bbf-94a2-f7964ca7514a | -8.70316 | -45.23238 | 2024-10-02 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ef155b8a-e73b-368c-b487-f57d44e0e4cb | -8.70255 | -45.23656 | 2024-10-02 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e0c755e5-ef50-3f19-a3fd-49adf6d00ea0 | -8.69916 | -45.23397 | 2024-10-02 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f234d782-392b-3121-b603-108625bf719d | -8.69859 | -45.23817 | 2024-10-02 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a74c7243-622c-3bdd-818c-b817c4b8678d | -8.69816 | -45.23613 | 2024-10-02 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c1f3e10-0449-3bbc-892f-90d5ba3ad819 | -8.69756 | -45.24032 | 2024-10-02 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1050b776-2d40-3b12-ab7e-dcb4ac05e625 | -8.69376 | -45.23565 | 2024-10-02 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d9cd0877-a15a-3f5f-934c-f55bca155998 | -8.69317 | -45.23982 | 2024-10-02 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 44a3f5d2-4c9e-3fef-bdb2-792433747a7a | -8.68878 | -45.2393 | 2024-10-02 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b7002b2-1826-39de-89f1-4fced55ad686 | -8.68818 | -45.24348 | 2024-10-02 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e8411a9-9701-33bb-a6c1-de3aa82916d8 | -8.63449 | -44.06201 | 2024-10-02 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4eaf8d5a-25b9-3cdf-863b-b17ebb6e556e | -8.63376 | -44.06723 | 2024-10-02 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c22e1414-4484-3a96-9677-3187785b0bd7 | -8.53214 | -44.7257 | 2024-10-02 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d4b80747-f5ae-38d5-a629-3c4591503aa2 | -8.46459 | -45.1089 | 2024-10-02 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 925048de-0fac-3148-a7a4-86d43ffddbac | -8.46019 | -45.10829 | 2024-10-02 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a16b46e0-fdb2-3e30-b951-56e57fd9d8b8 | -8.33726 | -45.33955 | 2024-10-02 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bf47d748-9efc-31f6-adb5-fbc41f0689e4 | -8.33668 | -45.34359 | 2024-10-02 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d5a2f57d-7d61-38e6-bc62-7731e0ed7f9c | -8.33181 | -45.34686 | 2024-10-02 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 21814417-3b60-3fa9-afc3-7a7799d50044 | -8.23452 | -44.34059 | 2024-10-02 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5891e110-b11e-3383-adee-500b1b628071 | -8.23319 | -44.35022 | 2024-10-02 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README86.md)
