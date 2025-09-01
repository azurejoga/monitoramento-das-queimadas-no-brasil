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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07339755-89a6-3420-b1c9-a0351c8780a7 | -11.045 | -47.0514 | 2025-09-01 01:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 155.9 |
| 8e220455-b310-3b29-9161-33d99717799d | -18.6704 | -52.5973 | 2025-09-01 01:00:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 45.3 |
| f57bf23f-9992-38bb-b198-13ca7ce45cf7 | -12.2094 | -43.8803 | 2025-09-01 01:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 103.8 |
| f69a5b5f-06f7-391d-a07f-7d2b3e7c8898 | -12.5722 | -48.2059 | 2025-09-01 01:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 9eaeec78-6489-355b-9794-7e486be93611 | -19.0724 | -48.3148 | 2025-09-01 01:00:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 7f04bc38-c12f-3827-a3a1-2c4dc204583b | -15.6916 | -48.9065 | 2025-09-01 01:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 253202b4-b057-3de0-8103-9b95232bca05 | -15.7116 | -48.8809 | 2025-09-01 01:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 39f9af5a-3f08-35b2-9b7f-41849ff3b6eb | -13.1644 | -45.2897 | 2025-09-01 01:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 38d4e9f7-b3d1-3a62-afd7-c8b5e5ac5914 | -11.3705 | -43.5868 | 2025-09-01 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 72.5 |
| f86b6ea3-cd75-3824-8611-2df91fef2cb6 | -17.615 | -46.684 | 2025-09-01 01:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 77.6 |
| dd2b39bd-5a81-3525-82e1-e25017e01234 | -6.8095 | -52.8154 | 2025-09-01 01:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| eb39b08c-0424-3d06-abaa-2322024bf663 | -10.0434 | -48.0998 | 2025-09-01 01:00:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 85e33928-7b45-33d9-9a59-c406daea6a45 | -9.135 | -65.5453 | 2025-09-01 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 20fcdc7e-ac2f-3c4e-99c2-df94218bcd33 | -10.5937 | -44.331 | 2025-09-01 01:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 2794c57d-9076-3494-a259-18ffdeb24715 | -11.0454 | -47.029 | 2025-09-01 01:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| eb8d0e99-fa73-3fa5-afe5-153e63207ad9 | -15.7112 | -48.9032 | 2025-09-01 01:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 148.7 |
| c3c73618-d7e7-3abe-81df-f2c81f93a975 | -15.7107 | -48.9255 | 2025-09-01 01:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 64.1 |
| ead034ad-be3b-395b-953a-753e60bea347 | -19.0718 | -48.3379 | 2025-09-01 01:00:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 998d8937-b0f1-3c20-b0a2-1400ebb3de4d | -11.3696 | -43.6341 | 2025-09-01 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 9e732552-4f74-373a-a354-8c1004b4b396 | -13.1648 | -45.2665 | 2025-09-01 01:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 12f9b452-14bd-3303-99ba-fa8982f6405c | -17.6155 | -46.6607 | 2025-09-01 01:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 89fd63dc-3eed-382b-878b-80fc3a73523f | -7.0946 | -44.3589 | 2025-09-01 01:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 118.1 |
| ea75fd38-0c32-3c13-949b-91ac313cd0b0 | -11.026 | -47.0538 | 2025-09-01 01:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 605.0 |
| 8d3aa7c4-6349-3421-a178-d48976af8f8f | -15.6063 | -48.3177 | 2025-09-01 01:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 634b5a71-519c-3707-9a52-3d079651d036 | -13.1837 | -45.2865 | 2025-09-01 01:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 30c2912d-c050-3d28-9da2-1e27c865be3e | -19.0522 | -48.3191 | 2025-09-01 01:00:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 68d7254e-85a1-3073-bd9d-3d274ad5100d | -7.6783 | -61.0908 | 2025-09-01 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 37.3 |
| c177843b-a6ff-3a53-a1aa-bbec1b22c6d8 | -7.0757 | -44.3606 | 2025-09-01 01:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 148.6 |
| d6868038-1e84-3318-8196-d1932d6d6a8f | -15.7173 | -48.99746 | 2025-09-01 01:07:00 | TERRA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 488f8e2e-4b94-3e64-b9e4-89f08f6c17fc | -22.249 | -56.09321 | 2025-09-01 01:07:00 | TERRA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 4b1580fe-6574-3eae-a4b7-6246dde0e039 | -19.06974 | -48.34448 | 2025-09-01 01:07:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 6f6076ed-fac0-33d1-8a85-44ac77676765 | -22.36376 | -52.14433 | 2025-09-01 01:07:00 | TERRA_M-M | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 33.2 |
| 1032221f-8e48-3369-b93b-081bcb4bcbd5 | -15.59289 | -48.31445 | 2025-09-01 01:07:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 3aa59597-d091-3cf8-aaf6-c0d1e7e72a74 | -19.06604 | -48.32378 | 2025-09-01 01:07:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 36.5 |
| f6cc537b-dff9-3dec-84a9-650f9605c458 | -15.3226 | -46.10989 | 2025-09-01 01:07:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 9b0eabae-ed5b-3aaa-b2e0-a030ac15d8e6 | -22.25033 | -56.10337 | 2025-09-01 01:07:00 | TERRA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 16ebfcde-3f1f-30a5-8169-719da1a0b9d3 | -17.61338 | -46.69592 | 2025-09-01 01:07:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 5ad65bba-3ff4-3335-96bb-f7355a5131b2 | -17.60963 | -46.67144 | 2025-09-01 01:07:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 582.9 |
| 6778c0de-8c59-3193-8c15-a11086a56ecc | -15.72077 | -49.01785 | 2025-09-01 01:07:00 | TERRA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 1d54d07c-ee60-3e5a-9797-f189d6fe31b2 | -15.72759 | -48.98923 | 2025-09-01 01:07:00 | TERRA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 7687931d-812c-30cc-8a32-68099bbe19a6 | -22.95034 | -49.98788 | 2025-09-01 01:07:00 | TERRA_M-M | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 19.6 |
| 623eeadd-e8e9-3427-aedc-549ae47ec810 | -22.36209 | -52.13352 | 2025-09-01 01:07:00 | TERRA_M-M | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 81.9 |
| fe0eef98-8edb-313f-b944-abb86db4b1b3 | -15.72593 | -48.90325 | 2025-09-01 01:07:00 | TERRA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 6b9ec31f-c171-3834-b11e-6acfcb6edbd6 | -15.60478 | -48.34175 | 2025-09-01 01:07:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 54.9 |
| b29c1b8f-0814-3a39-bf31-6646f161e925 | -15.703 | -48.91348 | 2025-09-01 01:07:00 | TERRA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 9ab48b2d-44ed-3962-a63b-35b887f47c7d | -15.60096 | -48.35902 | 2025-09-01 01:07:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 97.8 |
| ffa1dc9d-224c-384d-924c-c6b1520337e0 | -22.25419 | -54.88965 | 2025-09-01 01:07:00 | TERRA_M-M | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 36e22c22-549c-3aad-a4f7-a926387540d4 | -20.40724 | -46.42084 | 2025-09-01 01:07:00 | TERRA_M-M | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 27.9 |
| e5cf4b79-1707-381a-ad90-e0f8064dea91 | -15.59702 | -48.33727 | 2025-09-01 01:07:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 157.6 |
| 8357df52-c35c-3cdb-8a40-b83f20437ddb | -19.057 | -48.34724 | 2025-09-01 01:07:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 28.2 |
| cb55d575-5bde-3113-8287-99cbb06fdeac | -23.11933 | -52.55518 | 2025-09-01 01:07:00 | TERRA_M-M | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| c0fa6756-c0c0-3788-8068-bc1062f78116 | -15.59103 | -48.34428 | 2025-09-01 01:07:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 199.0 |
| b279d598-7bff-3e4d-bf1a-cd0a269fbfdc | -15.60075 | -48.31855 | 2025-09-01 01:07:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 7ea64e35-5343-3ea9-9336-b3d8691bc538 | -16.96836 | -49.30585 | 2025-09-01 01:07:00 | TERRA_M-M | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 6c8def9e-4d04-343f-aeb8-af2ad131a99f | -23.11629 | -52.53478 | 2025-09-01 01:07:00 | TERRA_M-M | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 55007afe-cff4-3681-aef2-4e0e4242362d | -15.71289 | -48.90612 | 2025-09-01 01:07:00 | TERRA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 399cfc3f-02ee-384d-a127-81f701f492c8 | -15.73026 | -48.99463 | 2025-09-01 01:07:00 | TERRA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 5672a936-1ff0-325a-89ac-171f68d13da7 | -15.58708 | -48.32166 | 2025-09-01 01:07:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 67cf24bc-01cb-37e5-bf11-7e989e33ec34 | -16.29 | -52.93461 | 2025-09-01 01:07:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 2890c586-eceb-39d7-91c8-1aec42bcf640 | -19.05326 | -48.3265 | 2025-09-01 01:07:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 913c21ed-c475-3175-a9f8-fd3289ec810d | -21.69044 | -49.11539 | 2025-09-01 01:07:00 | TERRA_M-M | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 1e46c7f4-2c2c-34f4-a4eb-1c3e0f488b64 | -15.69711 | -48.95805 | 2025-09-01 01:07:00 | TERRA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 07469871-dfc8-37b9-8854-29561c5528e3 | -20.97842 | -56.92148 | 2025-09-01 01:07:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 88305b8b-83f3-3be9-ae10-ec0e8573ec99 | -15.69346 | -48.93675 | 2025-09-01 01:07:00 | TERRA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 26.6 |
| d0cd22ff-82b6-3a8e-a5f2-d006bb1a13d6 | -15.59489 | -48.36637 | 2025-09-01 01:07:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 4818abd7-e3f3-38b2-a20f-7d48cce10acd | -17.61507 | -46.701 | 2025-09-01 01:07:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 56.9 |
| b602b6b0-9bc6-3342-9510-e3085edc7b5f | -23.7417 | -54.93875 | 2025-09-01 01:07:00 | TERRA_M-M | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 21ec2e96-e38b-3433-8b4a-a9a2b328201c | -23.11781 | -52.54501 | 2025-09-01 01:07:00 | TERRA_M-M | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 56.3 |
| af9ec225-d4a6-36cb-b0a2-40fda7ab685d | -17.60773 | -46.66638 | 2025-09-01 01:07:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 492.5 |
| 55d1bfd3-f001-33bf-9245-77b0f0906848 | -15.69947 | -48.90689 | 2025-09-01 01:07:00 | TERRA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 136.9 |
| a0dcc497-324b-3456-8f08-8a61a2393ed1 | -16.29175 | -52.94591 | 2025-09-01 01:07:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 15.8 |
| fc63261b-9008-3733-bf16-30ef9076992b | -15.71817 | -49.01191 | 2025-09-01 01:07:00 | TERRA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 1f30f6e5-4e15-34da-bc4d-8d53871c655e | -20.40889 | -46.41372 | 2025-09-01 01:07:00 | TERRA_M-M | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 33.3 |
| a7937a9f-2c77-398d-8f6d-c7fcbba64295 | -15.6895 | -48.91368 | 2025-09-01 01:07:00 | TERRA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 23.0 |
| f9d1855d-1102-3654-8fc2-5fd9ce46475d | -22.25289 | -54.88009 | 2025-09-01 01:07:00 | TERRA_M-M | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 559c972a-7580-31aa-bd16-e195590e9e14 | -18.66776 | -52.59738 | 2025-09-01 01:07:00 | TERRA_M-M | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 1ebcefec-2845-3270-85f7-69d551836f73 | -10.04884 | -48.1152 | 2025-09-01 01:09:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| c9ae79b7-3306-3438-94e2-4c524c3ebb3f | -12.92534 | -56.94376 | 2025-09-01 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| c9f1b379-6070-39cb-90b5-c7d0ad48e811 | -12.97555 | -54.75912 | 2025-09-01 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3800df66-99f0-3c77-b974-c96c4b39ad98 | -13.36464 | -51.73912 | 2025-09-01 01:09:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| f9260b14-a8f6-3709-abfb-e8d4f240163e | -10.84156 | -55.75289 | 2025-09-01 01:09:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 772880ca-23c5-3be4-addf-a346d5c04ec4 | -7.57771 | -63.04618 | 2025-09-01 01:09:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 64668cb6-da7f-3099-99d3-cc47cae7aa4e | -12.6117 | -57.01384 | 2025-09-01 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| b8779541-7bcd-3911-b332-370ef1cc998e | -6.80506 | -52.82129 | 2025-09-01 01:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| c070db99-fdce-3d28-b878-10761ed17acd | -14.59794 | -54.56469 | 2025-09-01 01:09:00 | TERRA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e461651d-7eb5-3910-8e5c-1fe64cba900b | -11.02466 | -47.02012 | 2025-09-01 01:09:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 8cb02d49-5022-32fd-8f94-e4565c956fac | -6.84852 | -52.80862 | 2025-09-01 01:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 88506d73-26de-3103-b289-1beefefd5fd4 | -14.6062 | -54.49385 | 2025-09-01 01:09:00 | TERRA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ceae5601-66ac-352a-acc9-38bcbbf74f2f | -11.88336 | -51.70332 | 2025-09-01 01:09:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 143e0755-54bb-362c-a0ea-d5d99b3cf927 | -6.34313 | -58.17754 | 2025-09-01 01:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e7c8d18e-b3c1-3be8-adcc-bace50ad1159 | -7.07576 | -63.07465 | 2025-09-01 01:09:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| f629a6b1-c5bf-3d7b-afad-a4435bfa4076 | -11.51625 | -54.47942 | 2025-09-01 01:09:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 7295b2a4-edf2-3035-bddb-724a5137926b | -12.92144 | -56.98127 | 2025-09-01 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| ca6b8096-3865-31f5-857b-3ed8d93337a0 | -12.9202 | -56.97221 | 2025-09-01 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 60f92d2d-bb9b-31d2-b3d3-3aa9a13301db | -13.36697 | -51.75374 | 2025-09-01 01:09:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5dca44b1-65fa-3e34-bfda-b9d66305e364 | -7.2784 | -60.6675 | 2025-09-01 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 396729f0-8129-324e-9347-27703fb04d07 | -6.80276 | -52.80607 | 2025-09-01 01:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| d4cf2112-3951-31f3-91af-a03e7c22ca2f | -9.28245 | -47.10226 | 2025-09-01 01:09:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| dd7bc1c0-0838-3696-a964-498e4d546540 | -12.90888 | -56.9554 | 2025-09-01 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 3bae6cf9-663e-3c39-8d35-3a97ecf67975 | -7.10679 | -63.03767 | 2025-09-01 01:09:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 26.5 |


[Clique aqui para ver as próximas entradas](README5.md)
