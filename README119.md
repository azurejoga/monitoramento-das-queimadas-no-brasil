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

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 033f8333-d941-3f9e-9153-b09c281eb80f | -7.21385 | -55.19896 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c72ca570-5a8d-3798-b97e-03c3839e0f2d | -3.27657 | -54.00787 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2d0fface-9d59-375e-84f7-72b4a87e219a | -3.69329 | -55.45913 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e7176ebc-1155-3300-bed4-f28833b62164 | -4.05898 | -54.03934 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 12ceb0c5-8ec0-3bd1-afc8-0bd03f603b04 | -3.18634 | -54.08224 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| fe5c8484-f88c-3a08-a660-b4229e1e5fb3 | -6.87901 | -43.67309 | 2026-10-05 17:15:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 04234800-ff4a-356c-9247-04b956bdf39e | -8.52549 | -54.60252 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 3461c3e1-e03e-3c96-acd7-af34ee22c3f6 | -6.07231 | -53.87303 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5140cf6-f297-362a-ada1-27b1f7b46631 | -3.03983 | -54.25023 | 2026-10-05 17:15:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 9be8ee5b-1622-348a-bc1f-f9f49cd1543d | -8.625 | -66.99908 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 834e47fe-cfaf-3c0d-8bb7-49a473001175 | -3.81961 | -41.79883 | 2026-10-05 17:15:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| eadb1ea0-ccaa-3202-bfc6-a313af35794d | -2.69627 | -49.03515 | 2026-10-05 17:15:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 57266be0-243a-384b-ba46-e2e5d1a2b721 | -9.10594 | -64.37799 | 2026-10-05 17:15:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 24.2 |
| f924de66-2ac8-3a34-9613-73f2c37a9cd2 | -5.83184 | -45.01437 | 2026-10-05 17:15:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| bc4fc744-ed35-3fed-a8de-b6e5dd20dffc | -3.09386 | -53.71752 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 109.8 |
| bd5a1b94-4bcd-3d8a-8c01-ddf1257bf3fd | -3.32997 | -53.38666 | 2026-10-05 17:15:00 | NPP-375 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 60943d45-08b3-3d5a-9d3e-a3e720541b77 | -5.81664 | -53.83574 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 04be7b6c-6bd9-3fa1-9490-65229c5afdef | -3.62722 | -55.28484 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 174.5 |
| e4913094-faa9-3040-9787-13871d6badcc | -5.88378 | -45.96839 | 2026-10-05 17:15:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| f091091d-6bc3-381e-868d-91fee8782fcd | -3.27936 | -54.00391 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b40c12bf-6725-34fc-a4ae-f636b23810c2 | -3.11835 | -53.70634 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 0c007b6e-988a-331a-9261-38224ddc73ad | -4.46571 | -54.97423 | 2026-10-05 17:15:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 7ee46bc2-5619-336c-abf6-854cce39ee76 | -3.12888 | -53.7083 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 69e47fcb-77f7-3a55-970f-4464987d5e86 | -3.7279 | -55.48305 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 9d03dda2-6655-35a7-90ee-00ba12f7da75 | -2.49107 | -49.40949 | 2026-10-05 17:15:00 | NPP-375 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| a81e069f-d50e-3486-ae53-cb750496b956 | -6.84888 | -41.79713 | 2026-10-05 17:15:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 32.3 |
| 0868180c-ff9c-32a9-aedc-ee2db9fbb112 | -3.10557 | -53.71184 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 110.8 |
| c42584a0-ad61-3ada-a654-c6cfb5d12ffc | -3.84535 | -50.31618 | 2026-10-05 17:15:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7ced5303-6ed5-3e2a-b334-e07c971465b4 | -8.20684 | -54.70755 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 176b055a-a119-3774-85e0-fae0f237c32e | -3.5118 | -54.61745 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 641bed77-6b53-39fe-96b5-793328f1f2e8 | -4.38095 | -43.9317 | 2026-10-05 17:15:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| b29f6b56-3c6c-3a1a-82c6-0864b009583a | -3.61048 | -54.59826 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1640fa9b-812b-3497-aab2-54365d27284b | -7.47916 | -42.80776 | 2026-10-05 17:15:00 | NPP-375 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 24.8 |
| 4fe0ae49-96f9-3c44-b15f-c688d0c76152 | -3.61433 | -54.60121 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 70977db1-013d-3a06-9e00-a58b66f2a041 | -4.8542 | -44.52228 | 2026-10-05 17:15:00 | NPP-375 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| c503df22-fb75-358d-b20e-d25e60f8158c | -9.80154 | -49.30579 | 2026-10-05 17:15:00 | NPP-375 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b686401c-e68f-3382-b174-c4acaa709ce2 | -9.29365 | -65.64834 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 2c2ef52c-a830-35aa-b5ec-0f2ddf9d7495 | -4.79465 | -42.5761 | 2026-10-05 17:15:00 | NPP-375 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 90aaaf86-c943-30df-9eb9-49fdb39f5c03 | -5.03445 | -42.76321 | 2026-10-05 17:15:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 86b411fd-e1e4-3e95-b3f8-4297f5e52950 | -5.81126 | -45.24141 | 2026-10-05 17:15:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d5f16dff-ae94-304f-b4d0-e5e6b456134a | -9.02086 | -45.16 | 2026-10-05 17:15:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 31ad1ac2-d483-358c-ab5e-ee86f0cea2f2 | -3.57416 | -54.64978 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 49874659-76ac-3bba-9a32-bf18117a85d1 | -8.5978 | -67.13371 | 2026-10-05 17:15:00 | NPP-375 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| c8d374e2-6367-33e1-8c99-b1e8b2d3beb2 | -10.19175 | -52.561 | 2026-10-05 17:15:00 | NPP-375 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 86b5666d-173b-3388-94cc-3e8099d75979 | -3.00875 | -53.86961 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7fb81cbd-57ec-320a-9405-66fce85d6326 | -7.21336 | -55.19921 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 1d8bf36e-feea-38a9-92eb-cf91a259c09b | -6.6807 | -45.20377 | 2026-10-05 17:15:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1afe1425-0727-3f63-850f-098b6c3fce29 | -3.69023 | -42.19312 | 2026-10-05 17:15:00 | NPP-375 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| d1b13ea4-f2f8-343e-80c7-c5c567b3ceda | -3.03809 | -54.26107 | 2026-10-05 17:15:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 125023fe-28d8-3058-9afc-c50148e9c0e1 | -3.97783 | -59.33731 | 2026-10-05 17:15:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2b0b171d-7b51-32dc-95ba-9abcd39e991d | -8.43433 | -54.99264 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 426a35c6-39bb-3ea4-87a5-eea1f73a996b | -7.20932 | -55.19214 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 70ca120a-079b-3f73-9187-5f02266c8524 | -5.55634 | -44.08019 | 2026-10-05 17:15:00 | NPP-375 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 33bd8891-88ab-38e4-9d70-a8566aabfb6a | -3.68784 | -55.95845 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 3250cecc-ea09-3dfc-a955-0c5487ab9178 | -6.49882 | -44.16858 | 2026-10-05 17:15:00 | NPP-375 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aa31a544-0c6a-3aa0-bd55-453b80777593 | -3.67484 | -55.94165 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.0 |
| 392ca28d-9cd4-3b65-9a74-b87b2b4af16c | -2.67277 | -49.03144 | 2026-10-05 17:15:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 40c0a31b-e595-3d47-93b2-0f9e6fac0135 | -9.0267 | -45.16465 | 2026-10-05 17:15:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 595856af-6935-3356-84a8-a1d55f4d68f4 | -3.52899 | -54.33154 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 168.2 |
| 19b2c6ed-02e5-3322-986d-71fa893f3b1f | -5.89584 | -55.52291 | 2026-10-05 17:15:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 7b6e359d-2408-3353-b968-38081062bec4 | -6.60348 | -41.57247 | 2026-10-05 17:15:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 7a246f37-c666-39a2-94c3-a570dfe00442 | -3.67478 | -54.53462 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 507c771a-ba0b-3446-a003-e3bd95d5ea8b | -3.07204 | -54.17406 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| c574069e-3527-37ac-a942-27d398cb7b79 | -3.09354 | -54.1814 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1bcb83ec-e178-313e-8045-2d1f59714a6b | -3.71941 | -58.20882 | 2026-10-05 17:15:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| ce65cde6-a26e-3a8d-a558-1d58a673a00c | -3.96441 | -55.48002 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 905c4168-4e0b-366e-a24f-710ef5560c6e | -2.97929 | -41.80103 | 2026-10-05 17:15:00 | NPP-375 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e058e4e1-6366-31a4-a8cf-e1e851d2a398 | -3.55883 | -54.4824 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| b5ceb480-b8da-3ec3-87aa-1afbd3f90e6e | -3.51391 | -54.63129 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 125.8 |
| ef57f7dc-f101-319b-9bec-d29f2b6ef842 | -6.14095 | -53.8157 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 92f9bc16-1762-329e-9649-57dc16042252 | -7.90073 | -44.20935 | 2026-10-05 17:15:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 579461a5-5162-3e6b-8518-89a415f09be6 | -6.93119 | -43.67562 | 2026-10-05 17:15:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 15.4 |
| ff55a95b-cb7b-35f5-9871-c6e4051d32a1 | -4.78142 | -42.57331 | 2026-10-05 17:15:00 | NPP-375 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 651f5df3-a7f8-32d5-9649-7007d9b0c0e0 | -3.0445 | -54.21423 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8112678d-47e2-3a9d-9579-da17cd5a28cd | -7.47993 | -42.81194 | 2026-10-05 17:15:00 | NPP-375 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 24.8 |
| 09265d28-7bd7-3566-8312-fd624ad2980d | -8.86598 | -66.79678 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 37c87a4c-6532-330e-b29f-a507d8839773 | -7.22252 | -55.19028 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5e9bcb86-beca-3366-8c5a-8f06436b2a6f | -4.35694 | -43.82571 | 2026-10-05 17:15:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| d204e02b-ecc6-36af-a49d-e6936bda05de | -3.10105 | -53.72676 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| b4bab492-dc61-314f-8c6a-7465f5409632 | -3.37514 | -54.10149 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 58d30760-55fc-3fbe-899a-77e395489328 | -6.64301 | -55.32301 | 2026-10-05 17:15:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4f56dcde-7acd-3d84-9ec7-df76ed28b4cf | -6.90625 | -43.66458 | 2026-10-05 17:15:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 6bff8d5f-3280-392f-a9ff-1d659e005363 | -8.53385 | -54.58291 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e0d553da-eb84-3de5-932c-ba5f52afef0f | -6.46447 | -43.59224 | 2026-10-05 17:15:00 | NPP-375 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ec12529e-7b44-36f7-81ed-2323c5c2cf77 | -6.60444 | -41.57764 | 2026-10-05 17:15:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 27.4 |
| 003628f7-dc70-3480-af34-c301ab82335c | -3.50969 | -54.60363 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 26107c68-999a-32e2-baca-685756dd6bf6 | -3.7303 | -54.65357 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 84c7603d-525b-35eb-9116-9a50e71b0694 | -9.81926 | -65.01657 | 2026-10-05 17:15:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2e911ea2-e31a-3de7-bd83-689eee7fb24b | -6.69721 | -45.2196 | 2026-10-05 17:15:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 52a252d6-05e5-3a94-be19-312800d5720d | -3.01855 | -53.89231 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 60ae6fd9-98e1-3fdd-8452-db0e07553288 | -3.23816 | -53.86861 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0955603e-8e66-32cd-acb8-0e0848ca49af | -9.13853 | -65.91292 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 15ea5090-7ba4-3b0e-be4f-18848fd9a053 | -3.60089 | -54.05148 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| da8a0fa2-3b5e-32a9-87f6-44221fb23b76 | -6.70997 | -45.23302 | 2026-10-05 17:15:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a4438e8b-36de-3992-9df7-75d9b57f2194 | -4.78929 | -42.58187 | 2026-10-05 17:15:00 | NPP-375 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 4c1f3099-634c-32cc-bc05-d4f45567a1da | -6.88103 | -43.68435 | 2026-10-05 17:15:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 5cc04919-0954-339e-9268-559a666a758d | -4.95754 | -40.56861 | 2026-10-05 17:15:00 | NPP-375 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 21.7 |
| 54f66e91-0f6e-34b8-bd91-15a1d71d0d3a | -4.0672 | -54.04869 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 5106ef7e-cc31-3a12-a5b4-2eb8de6ed69c | -3.87014 | -40.20108 | 2026-10-05 17:15:00 | NPP-375 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 7c38c93c-9b5a-38a0-9cf7-47f3338df020 | -7.22593 | -55.18977 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |


[Clique aqui para ver as próximas entradas](README120.md)
