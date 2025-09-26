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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1329b4ba-5eb8-3c29-b3b8-18854b659b81 | -9.6957 | -48.94641 | 2025-09-26 04:42:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b69810ae-bf61-3758-a0c3-697916975b87 | -8.78695 | -43.06284 | 2025-09-26 04:42:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 32d8479a-4bf0-3cbc-a8be-4b503c842713 | -4.51103 | -50.79976 | 2025-09-26 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9ecb2c08-04aa-3475-bd36-8285739151ff | -7.12918 | -42.20156 | 2025-09-26 04:42:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7a868d5a-a76f-3a40-8c1a-dc138d668255 | -8.19588 | -46.38691 | 2025-09-26 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1bc17b07-d257-3953-a381-542cb981c017 | -9.00358 | -44.10899 | 2025-09-26 04:42:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30cb6ff4-7f5f-3252-8d85-28a7699155a9 | -8.14104 | -42.37627 | 2025-09-26 04:42:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fc687ae2-e47a-3a08-a90c-1d4cd461707b | -10.56751 | -44.07891 | 2025-09-26 04:42:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c194eb4e-fd98-3865-98a6-33e04e197ac2 | -5.74906 | -44.96299 | 2025-09-26 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 00be65ea-de5d-32f5-8d69-f6441bdaee20 | -6.8552 | -43.18354 | 2025-09-26 04:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c36cc585-0ba5-3bff-8dc8-6451f7632150 | -9.87041 | -48.87366 | 2025-09-26 04:42:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ac1cced-e87a-3184-a614-fbb098c10209 | -8.50961 | -44.62038 | 2025-09-26 04:42:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae894e71-20b6-3dc2-9274-bf6aefa4a904 | -3.82989 | -50.97313 | 2025-09-26 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9db156ad-c4d2-3a7e-9758-ba22ead82de2 | -3.84089 | -50.97095 | 2025-09-26 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60e183c6-4b68-3e23-8a00-26c416b80b7a | -6.26536 | -42.4842 | 2025-09-26 04:42:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 721005c5-2476-3176-8ba7-80175111c4c9 | -7.80503 | -46.17682 | 2025-09-26 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1cec94d9-8a07-31d1-9db2-191a9c5038ac | -5.78347 | -42.87325 | 2025-09-26 04:42:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| df544983-8324-3d94-a107-5214e77a0aa0 | -7.77811 | -47.39903 | 2025-09-26 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5aa5dabd-8b75-3362-8dbe-879a847ed6fe | -7.80933 | -55.22455 | 2025-09-26 04:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b21d776-c3a9-3a41-9263-e411022a9b6b | -5.59865 | -45.37551 | 2025-09-26 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5bcae483-6225-39d2-8678-8ab5227f0d7b | -6.63931 | -43.82723 | 2025-09-26 04:42:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64647662-1249-3d29-9729-ba82936e85d6 | -4.35832 | -47.50581 | 2025-09-26 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 75d9e966-268d-3fe0-ac4b-c7da0b226936 | -7.68163 | -45.99265 | 2025-09-26 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8a4f993e-8269-3ad9-9dd8-9262377c2c13 | -7.25482 | -43.02118 | 2025-09-26 04:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 241b2f55-3eb2-333b-9c93-5397f2e79127 | -7.38747 | -39.11693 | 2025-09-26 04:42:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1f7f6ea4-9ac7-38a0-927c-0396591e7cb2 | -5.76558 | -42.55374 | 2025-09-26 04:42:00 | NPP-375D | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a8b57894-7246-3861-89f5-409985628db5 | -4.81061 | -43.53868 | 2025-09-26 04:42:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2cc960a2-52af-315f-96e2-d064f342edbe | -8.19303 | -46.39334 | 2025-09-26 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ba835d5-3f43-37f6-92ac-c9141ea28b22 | -8.72838 | -45.42271 | 2025-09-26 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2801484-6774-387c-9a7f-9c6f9e92405d | -8.94774 | -48.66113 | 2025-09-26 04:42:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6e0e3798-2950-3a49-a3ff-1c18efc09757 | -7.64415 | -45.9869 | 2025-09-26 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1eb77768-ba86-3a45-9f3c-1bf5d99de6ae | -10.59114 | -44.06691 | 2025-09-26 04:42:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2750b0d3-6685-3014-8b60-86332bc75f14 | -10.19213 | -44.84638 | 2025-09-26 04:42:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3789f5fc-400e-341c-979e-fac0b37d297e | -9.4422 | -40.37896 | 2025-09-26 04:42:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1029f2c3-29e8-3fe7-a71d-0d263e349420 | -10.28446 | -45.22084 | 2025-09-26 04:42:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7b708af-fa51-32d2-9dfa-16c348c96ce1 | -8.19736 | -46.38953 | 2025-09-26 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d153899-1747-33cf-8070-e6550741b037 | -6.59482 | -41.92257 | 2025-09-26 04:42:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 74cdb700-41de-31ac-8fe6-eaed10b558e2 | -6.55819 | -43.53234 | 2025-09-26 04:42:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9bdceb17-2dda-3ebe-821c-750f71df5c79 | -10.00747 | -44.17959 | 2025-09-26 04:42:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ac31cf0-b4e4-3e2f-913e-04cf0d476a65 | -5.12518 | -45.50175 | 2025-09-26 04:42:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41ef9691-3d13-3219-a762-d492e45bdb2a | -5.42726 | -41.3171 | 2025-09-26 04:42:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ec9135ec-df7a-3d92-8793-703c66c668c5 | -8.78659 | -43.06092 | 2025-09-26 04:42:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4c074f5a-b480-3811-b2f8-4e8befc612ac | -5.80215 | -42.80916 | 2025-09-26 04:42:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 42429d6c-47ae-3ea1-877c-d9d355f892b6 | -5.61677 | -43.46347 | 2025-09-26 04:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 18605a53-4617-3753-ac42-6031255ad789 | -10.39062 | -46.1339 | 2025-09-26 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86e788c2-5b6a-3265-b441-141d1a7eb3d0 | -4.74863 | -43.26727 | 2025-09-26 04:42:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cee200a4-4a4b-3968-a3de-27e439d5548a | -5.22988 | -46.08936 | 2025-09-26 04:42:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9da9da3f-4486-3da3-b8ef-1e09980bf43d | -6.71291 | -42.74073 | 2025-09-26 04:42:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ee223e48-e1e6-3aa4-ba4a-8b56e4e282d4 | -4.4268 | -47.26636 | 2025-09-26 04:42:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60ff08d1-dfd6-3726-93cb-d1af51d319a2 | -3.84149 | -50.96721 | 2025-09-26 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f38ba672-6d0d-367c-bcf2-e61e981c8657 | -10.14723 | -45.33817 | 2025-09-26 04:42:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f042cbb-122a-33d8-91c6-656e294a9e20 | -6.1377 | -44.87109 | 2025-09-26 04:42:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f05f8f61-7b76-3459-9c2c-52ed8fa19d28 | -7.59065 | -44.10949 | 2025-09-26 04:42:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c2fc799-9fc4-32b0-ae3f-62a04cf96dc5 | -7.67788 | -45.99206 | 2025-09-26 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6fdde886-5942-358c-8d80-c671b95fc563 | -6.13187 | -43.44948 | 2025-09-26 04:42:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7e2172f5-5e8a-30d5-94e1-ef62bdccccd9 | -6.96978 | -42.30148 | 2025-09-26 04:42:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 25ac90a9-72ce-37da-afbd-7985e80dbe23 | -7.81779 | -46.89628 | 2025-09-26 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee149713-3f84-3f15-80b3-e0a627f805dd | -5.42648 | -41.32257 | 2025-09-26 04:42:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bd53b621-87d3-38d9-94ea-c196c0bcc052 | -5.45934 | -43.06747 | 2025-09-26 04:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 635cb0e0-4bab-3ccf-9438-c5e1c7de450c | -8.78761 | -43.05828 | 2025-09-26 04:42:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 866a382e-9ab2-3c5e-b8c5-ea0bf2b1750c | -7.31032 | -45.77182 | 2025-09-26 04:42:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 112caebf-6445-3108-9c42-55aca9fba4fb | -6.85199 | -43.17416 | 2025-09-26 04:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1b364109-14dd-3fbc-b1d7-f0feb1982950 | -4.74366 | -43.61432 | 2025-09-26 04:42:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9c334769-416b-3b27-a5c9-2e3e0d77a1ee | -9.04834 | -50.11444 | 2025-09-26 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0fc508ff-baa9-3036-a16a-fb6827c2e6b7 | -6.59618 | -41.92006 | 2025-09-26 04:42:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| d9c4d697-ceb1-3acf-af1a-17f9c105f37b | -5.75078 | -44.97807 | 2025-09-26 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ab29d1e5-541f-3ded-b9bf-5c9ea65ad6b5 | -9.80424 | -45.7197 | 2025-09-26 04:42:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19d69762-ddef-3060-8e93-70c85688f915 | -9.93602 | -48.79041 | 2025-09-26 04:42:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10190c15-bbf6-3326-b6ae-b0d275bfc2d4 | -8.76989 | -43.05062 | 2025-09-26 04:42:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d706167e-b052-3d59-a3d9-1e1c27bbca4b | -4.98179 | -48.6736 | 2025-09-26 04:42:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 941f231f-ecf2-3adc-a8ed-a7365e18004b | -6.15026 | -47.28178 | 2025-09-26 04:42:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 325ff6df-3b02-3f6f-bed4-077d6b5203ef | -5.24618 | -43.08514 | 2025-09-26 04:42:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e90dba52-a412-3bf8-b2bb-e21999038666 | -10.40166 | -46.17698 | 2025-09-26 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 137723ef-46f4-3477-9b7e-04a91a044e08 | -7.28544 | -42.97709 | 2025-09-26 04:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5c460138-ecb8-3298-a641-8c811d19aa3c | -8.66241 | -43.99786 | 2025-09-26 04:42:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6d9f8c9-c321-33fa-a998-57171c7af0d8 | -10.12243 | -45.30995 | 2025-09-26 04:42:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c70ebf18-1ac3-3379-b5ac-86eb98fa4cfa | -5.63441 | -43.92685 | 2025-09-26 04:42:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 67ae352d-8c97-3b9a-93df-563874770f5e | -5.79967 | -42.79506 | 2025-09-26 04:42:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 6a2d6fc8-c08b-3e65-ac38-d48ce00eb5e7 | -5.53493 | -43.8748 | 2025-09-26 04:42:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7c93c0d9-1004-3dfb-92a3-7885c7210c08 | -5.79195 | -43.82654 | 2025-09-26 04:42:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2032e52-38e0-3f49-8244-a0df47e6409b | -4.81395 | -42.74232 | 2025-09-26 04:42:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ad84d6b-8eb2-33df-b818-29f4abeea98d | -10.01301 | -44.17185 | 2025-09-26 04:42:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0eb0d015-afe1-382f-b7ee-d2db4141fd5b | -8.9342 | -48.65902 | 2025-09-26 04:42:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ed52a28d-b3bd-3582-abec-5f0114a10a86 | -9.9377 | -47.44757 | 2025-09-26 04:42:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd9c1df1-09b9-366b-a6e9-499e734dced7 | -3.8189 | -50.97525 | 2025-09-26 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 59ef160c-0bec-36a1-a448-1beb6e60cda1 | -5.62914 | -43.9337 | 2025-09-26 04:42:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f1b789b5-40bc-32a0-98ce-2134869b7702 | -9.48871 | -40.35359 | 2025-09-26 04:42:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a75bc41d-728e-39d8-8c65-e3a6202493a8 | -10.39419 | -46.14664 | 2025-09-26 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 83f2d47c-82bd-3b05-9354-b481315b9bfd | -5.48481 | -50.1289 | 2025-09-26 04:42:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 49183049-1ccb-307f-becf-449fb5c89e40 | -7.38978 | -39.11284 | 2025-09-26 04:42:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ae65f8fa-cdd5-3b67-9ec6-fb7a1017ad42 | -10.00806 | -44.17542 | 2025-09-26 04:42:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 933730e4-0a19-3db3-9f9a-2b1ece23f31b | -8.7857 | -46.59329 | 2025-09-26 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1fb698f2-5c04-32f7-a99d-403565fe6aa7 | -5.53079 | -43.87412 | 2025-09-26 04:42:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1d11da29-f553-3c5e-a068-c936677e5e4c | -9.3379 | -48.54331 | 2025-09-26 04:42:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b09a694c-0842-332f-89be-345a4ea2944f | -7.11014 | -43.74464 | 2025-09-26 04:42:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| efb882ca-eea0-3794-8f69-9cb18bcf86fa | -6.70144 | -51.42458 | 2025-09-26 04:42:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f8e80e44-9395-3746-8470-182f527b948c | -8.07628 | -55.22396 | 2025-09-26 04:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40acec0c-0bc7-30f0-a365-4d65f5d6c8e4 | -8.50023 | -49.54474 | 2025-09-26 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf2d41ca-e613-3f6f-889a-6d9b7272a76d | -9.00844 | -44.10565 | 2025-09-26 04:42:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1034d2a-e52f-3a30-a966-f348a920d74d | -5.79186 | -42.81677 | 2025-09-26 04:42:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |


[Clique aqui para ver as próximas entradas](README29.md)
