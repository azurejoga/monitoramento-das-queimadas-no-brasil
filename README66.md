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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08347175-c03c-34b6-b502-f70601f898b5 | -21.76629 | -45.45757 | 2025-09-14 05:10:00 | NPP-375D | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 888f9a18-ddd0-361c-b977-0edf5c046b90 | -16.56083 | -55.19021 | 2025-09-14 05:10:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ad8c58b7-ca6f-3af6-936b-a62b91c4ecfa | -18.6394 | -51.79817 | 2025-09-14 05:10:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cfed7b04-2172-3c1f-81d6-3c82a4a842e4 | -20.56697 | -54.59293 | 2025-09-14 05:10:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9eb9599d-0772-3e93-b3aa-bf6c644f0fe2 | -15.7697 | -53.48333 | 2025-09-14 05:10:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bcd3edb4-2e65-32b3-a11a-664f32ee2ee3 | -15.76516 | -53.48757 | 2025-09-14 05:10:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9bf4e884-0252-3f5f-919f-cc6dfba34d42 | -15.78133 | -52.22222 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1e46a1b1-7bb8-3730-8717-efe69d97c100 | -15.57441 | -54.73586 | 2025-09-14 05:10:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6179450-a2c3-30c3-bae8-77c7b7fb3f2f | -17.40797 | -49.26261 | 2025-09-14 05:10:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c00b82f6-f20a-3d98-9b9d-89b9d58ab90d | -17.79397 | -51.73007 | 2025-09-14 05:10:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 858ec908-478f-35d3-a0b3-11b169f7252f | -15.52568 | -48.52522 | 2025-09-14 05:10:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0c46d1f0-5e65-3736-8f80-27537dafa155 | -15.77039 | -53.47834 | 2025-09-14 05:10:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 34ec0aeb-5908-34bc-8798-8771c7ad94f2 | -15.30915 | -59.24639 | 2025-09-14 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4781958d-c1aa-3c12-947d-0431593ca848 | -15.80058 | -52.20582 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 488f1d7e-c501-3d67-abc3-ed08170080c9 | -20.72417 | -56.73925 | 2025-09-14 05:10:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bb2f0a41-e3a6-32cb-bb84-9d0987b529a2 | -14.75375 | -60.2371 | 2025-09-14 05:10:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6303541e-3c5e-3592-b93f-64d0717c940c | -15.77241 | -52.22504 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 98bd04db-bbf2-3018-989c-4086af1b787b | -15.60501 | -54.77975 | 2025-09-14 05:10:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3926e0db-d130-3a4d-bcc5-31caf651df11 | -17.13167 | -48.51104 | 2025-09-14 05:10:00 | NPP-375D | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4d7984b9-3067-39e7-96f5-1d76f41caa30 | -17.43335 | -49.22053 | 2025-09-14 05:10:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3458c6b7-62c4-34c2-8e0c-edf74f36649d | -15.29172 | -53.77123 | 2025-09-14 05:10:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9c9dfda-e60d-3a16-87ff-ae137728eb80 | -17.14311 | -53.88968 | 2025-09-14 05:10:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d7f5599-3c59-35ef-853e-7d88d2feb2e5 | -20.12037 | -46.87813 | 2025-09-14 05:10:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c6493f94-a5ed-3d1b-9081-68b9514f0423 | -22.22513 | -48.61322 | 2025-09-14 05:10:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 2b1349eb-8308-3e13-9149-20ecc6f76701 | -16.24855 | -56.63253 | 2025-09-14 05:10:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 8cdb1761-048b-3e1b-ae77-ff11573f1c90 | -18.15552 | -49.20067 | 2025-09-14 05:10:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8bd7c82f-ec34-33cb-b5e1-1b716aac8bab | -16.71145 | -54.96375 | 2025-09-14 05:10:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1c6d043f-f253-3af8-9010-524ac9305f54 | -17.43858 | -49.22139 | 2025-09-14 05:10:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41dfb067-8533-3188-9c61-068ad15165cc | -16.3603 | -51.7673 | 2025-09-14 05:10:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 277ea2b5-280a-3b5a-bbcc-71df11ed95fa | -20.08254 | -46.90235 | 2025-09-14 05:10:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20c06dd3-0f4a-32eb-93c0-60f279e384ee | -22.19499 | -49.60759 | 2025-09-14 05:10:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f610b0ae-f866-343e-a272-9bf51326f142 | -16.49726 | -55.16131 | 2025-09-14 05:10:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| bc612cd5-937c-3ac2-91f3-522bdc11fe1a | -18.15585 | -49.19757 | 2025-09-14 05:10:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 022d22bd-6e5b-3e1d-9f8a-363fb0d04055 | -15.93167 | -49.97922 | 2025-09-14 05:10:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 70e31a8d-7631-3fda-983b-906c2b3fa2ec | -18.15211 | -49.1944 | 2025-09-14 05:10:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 684cdd52-c376-3f14-8a9f-3217b613a97f | -21.64316 | -50.20076 | 2025-09-14 05:10:00 | NPP-375D | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a8e0fdfb-46da-3ed8-92dc-b962616e8f32 | -17.2613 | -47.25083 | 2025-09-14 05:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5ada7074-a20d-3d29-b28c-3e79c7c27885 | -15.78133 | -53.48512 | 2025-09-14 05:10:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0884f80c-0837-350f-8967-53575451f22a | -17.36226 | -52.9076 | 2025-09-14 05:10:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0c0db5e-1f55-3a89-bf26-2511a6df0773 | -15.2811 | -56.02414 | 2025-09-14 05:10:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 064b43c4-6af2-3094-82eb-b74d1e13cd9a | -15.93498 | -49.97285 | 2025-09-14 05:10:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b7b52228-68bd-369b-ac9e-1de032335c16 | -21.62833 | -46.81578 | 2025-09-14 05:10:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 530ebfe1-01f2-367a-8024-642978a2e327 | -15.57308 | -54.77093 | 2025-09-14 05:10:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd21b230-ee6f-3537-8e9e-1342da2286c1 | -15.55076 | -54.79808 | 2025-09-14 05:10:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 83ca6dd7-9fd6-3279-9037-699b3148b35f | -15.77346 | -52.21687 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a5539fc-4230-3f72-b3ef-2cac621d6a1e | -17.32067 | -46.08775 | 2025-09-14 05:10:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ab04e9cb-36b7-3053-b623-449ba726c057 | -15.78202 | -53.48019 | 2025-09-14 05:10:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7ca8df10-769c-3315-af62-11a2011e9e3d | -17.27757 | -46.12177 | 2025-09-14 05:10:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f21c90cf-18c0-37c9-bbc4-98bc6b44c7c8 | -18.15519 | -49.2038 | 2025-09-14 05:10:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 48f0eae4-0e98-387a-ba83-f2beef1af5a5 | -15.19799 | -52.49348 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 909e2c37-78ed-3cc5-9e94-139e79949d94 | -15.76404 | -52.22368 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5bfb8bec-e0a4-3639-bdc0-de243941e722 | -17.3873 | -52.92527 | 2025-09-14 05:10:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1418484f-83c0-34ac-a5bf-fd8e511f40fa | -16.33357 | -51.52369 | 2025-09-14 05:10:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3990ec6f-986f-384d-986f-d2bdf7c0d6a0 | -18.01374 | -46.97399 | 2025-09-14 05:10:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7edb608a-49f2-30f4-8d53-bfd68d6dd9b3 | -23.47357 | -50.84987 | 2025-09-14 05:12:00 | NPP-375D | ASSAÍ | PARANÁ | Brasil | 4101903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 9f38748a-2cb4-3aaf-bb03-ed245c7d1489 | -23.47576 | -50.84869 | 2025-09-14 05:12:00 | NPP-375D | ASSAÍ | PARANÁ | Brasil | 4101903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 44937cc7-04b9-3181-952d-818dc3d056cf | -22.65728 | -53.11293 | 2025-09-14 05:12:00 | NPP-375D | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3cf518ca-29d4-3446-adb3-9b3dd33d6342 | -23.4805 | -50.85269 | 2025-09-14 05:12:00 | NPP-375D | ASSAÍ | PARANÁ | Brasil | 4101903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| aafdc976-cb52-3bbe-b90b-1ff55fb2a5df | -22.6578 | -53.10848 | 2025-09-14 05:12:00 | NPP-375D | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4b4104d6-a70b-3add-9d90-86103a516ced | -23.47543 | -50.85181 | 2025-09-14 05:12:00 | NPP-375D | ASSAÍ | PARANÁ | Brasil | 4101903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 182025da-f843-30bb-bbf5-3b03488e1c6a | -23.7955 | -49.94557 | 2025-09-14 05:12:00 | NPP-375D | TOMAZINA | PARANÁ | Brasil | 4127809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 76e77b92-f7d9-3331-b058-990fdb067554 | -23.84183 | -55.18592 | 2025-09-14 05:12:00 | NPP-375D | SETE QUEDAS | MATO GROSSO DO SUL | Brasil | 5007703 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 541aa91c-ac8b-3e0e-89f0-22c160d4e1a8 | -23.47386 | -50.84678 | 2025-09-14 05:12:00 | NPP-375D | ASSAÍ | PARANÁ | Brasil | 4101903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 97b34a1d-cd43-38cb-b97d-821bc6648370 | -22.9751 | -46.774 | 2025-09-14 05:12:00 | NPP-375D | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| d955795c-26d3-38da-ba3a-a2615b19404d | -22.72986 | -49.89238 | 2025-09-14 05:12:00 | NPP-375D | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c660711a-e72a-31c7-ac74-d99761a12f18 | -22.03108 | -55.87535 | 2025-09-14 05:12:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5379d122-96fd-30b0-b6fd-525b547b05b4 | -23.48083 | -50.84949 | 2025-09-14 05:12:00 | NPP-375D | ASSAÍ | PARANÁ | Brasil | 4101903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0d7d24b2-812b-3382-8068-c4048d63b8dd | -22.22828 | -56.0582 | 2025-09-14 05:12:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf981a8c-a400-3010-846b-ede4ebe4ac1f | -22.73237 | -49.89373 | 2025-09-14 05:12:00 | NPP-375D | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f081019f-38ff-31ed-944e-b42f31836fdf | -22.73737 | -49.89795 | 2025-09-14 05:12:00 | NPP-375D | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ed972de-5fe7-3ec5-9798-8a2d815db75a | -22.73272 | -49.89017 | 2025-09-14 05:12:00 | NPP-375D | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c32d24b-bf51-34df-8dde-cd259c4a83fd | -23.47834 | -50.85383 | 2025-09-14 05:12:00 | NPP-375D | ASSAÍ | PARANÁ | Brasil | 4101903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 8701814b-6ad3-3334-8f34-eef8b03579f2 | -22.52379 | -52.99721 | 2025-09-14 05:12:00 | NPP-375D | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 73c4ad7a-59fa-3ff7-8f9c-cfb09014cfe2 | -22.727 | -49.89312 | 2025-09-14 05:12:00 | NPP-375D | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e91ae43f-54ef-36cd-afe2-e8cbe48bb9fd | -22.6693 | -53.12361 | 2025-09-14 05:12:00 | NPP-375D | SÃO PEDRO DO PARANÁ | PARANÁ | Brasil | 4125902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| ec88f829-0c3f-37d7-92b0-b397ccec57c1 | -22.73522 | -49.89308 | 2025-09-14 05:12:00 | NPP-375D | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20398fc9-d429-3ed3-8756-ce83ac30742d | -22.02971 | -55.87728 | 2025-09-14 05:12:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f16593e-3120-3027-b3b4-f83674241c72 | -22.72735 | -49.88959 | 2025-09-14 05:12:00 | NPP-375D | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc17bf6a-bba4-3554-8b57-f038e3db9796 | -23.47895 | -50.84745 | 2025-09-14 05:12:00 | NPP-375D | ASSAÍ | PARANÁ | Brasil | 4101903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 30df32be-fc01-3e0a-bbf2-e9f1e9f7f4f3 | -22.97499 | -46.77376 | 2025-09-14 05:12:00 | NPP-375D | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 189d4b2b-ab85-38d0-9ceb-2a4826054492 | -23.77717 | -51.64238 | 2025-09-14 05:12:00 | NPP-375D | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ba3f8aab-9c05-36d9-94ce-cd06ce3e13fb | -23.47864 | -50.85066 | 2025-09-14 05:12:00 | NPP-375D | ASSAÍ | PARANÁ | Brasil | 4101903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| afd4ba30-94aa-34fb-838f-d42786421539 | -22.22755 | -56.06041 | 2025-09-14 05:12:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 95991fd7-d5ea-3f2a-85a0-785a8b840f05 | -22.66495 | -53.12301 | 2025-09-14 05:12:00 | NPP-375D | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8d6bced4-a79c-37e9-bbd2-1cfc0abd2aca | -23.47512 | -50.8549 | 2025-09-14 05:12:00 | NPP-375D | ASSAÍ | PARANÁ | Brasil | 4101903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 4f82560a-b679-3dbb-be47-1b3e802b9e50 | -24.08194 | -51.06995 | 2025-09-14 05:12:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 53bd2609-c113-3c2d-a0fb-f13204df1a28 | -24.07818 | -51.0697 | 2025-09-14 05:12:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 408af980-a80a-3cf5-8516-3abe805776b7 | -22.66111 | -53.11797 | 2025-09-14 05:12:00 | NPP-375D | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c13c932d-9729-3faf-9f67-4777c3661862 | -22.51554 | -52.99145 | 2025-09-14 05:12:00 | NPP-375D | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ef012519-5b09-340f-9610-d30f146154da | -22.73489 | -49.89663 | 2025-09-14 05:12:00 | NPP-375D | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 26ca782d-1e9c-3786-8bca-bb7969cc35bb | -22.51941 | -52.99653 | 2025-09-14 05:12:00 | NPP-375D | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c44b7090-212e-3b04-b7d0-6c8e056da3ee | -23.55407 | -51.55771 | 2025-09-14 05:12:00 | NPP-375D | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3bc00b19-80c8-3637-b167-077a3f8ed66a | -22.66547 | -53.11857 | 2025-09-14 05:12:00 | NPP-375D | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5f4cfefd-76cd-3206-9262-d4993a31db7e | -22.22765 | -56.06274 | 2025-09-14 05:12:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7569304-8b21-3a82-9f8c-369b4fd9c11c | -22.52328 | -53.00163 | 2025-09-14 05:12:00 | NPP-375D | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 5eff83a6-f3b3-32cc-9eae-cfd16de5336c | -23.74419 | -54.53189 | 2025-09-14 05:12:00 | NPP-375D | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8167de9d-d8d5-36eb-87c6-f3731e110f2a | -27.31567 | -51.8533 | 2025-09-14 05:12:00 | NPP-375D | CONCÓRDIA | SANTA CATARINA | Brasil | 4204301 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1aa93a80-fdac-3448-86b4-07160e50b271 | 3.00024 | -51.44777 | 2025-09-14 05:25:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6d3bb037-6f0c-3fa8-b8e2-cbce6da4f6a5 | -1.41639 | -48.39138 | 2025-09-14 05:25:00 | NOAA-20 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c3488b70-f0bf-331d-9923-fa7ef44de4a0 | -1.41729 | -48.38551 | 2025-09-14 05:25:00 | NOAA-20 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README67.md)
