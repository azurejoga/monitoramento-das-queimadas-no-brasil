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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63ac7037-98bf-3868-aa09-2859714ef830 | -6.0232 | -46.6784 | 2025-09-04 12:30:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 2ce105b9-6388-3aee-89c5-0ddae5f656b0 | -7.7036 | -48.7587 | 2025-09-04 12:30:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 1abf36f3-6180-3cf3-9247-d77a39247bd1 | -8.0417 | -45.3882 | 2025-09-04 12:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 814a8a45-3e5a-3d3a-b879-25e934c4bb0e | -13.8457 | -47.9764 | 2025-09-04 12:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 591fabd6-ec54-3844-b832-eb19d14a7e84 | -6.0232 | -46.6784 | 2025-09-04 12:40:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| f01e166d-6c5c-373b-83cf-e23111e2e17e | -8.3832 | -48.3099 | 2025-09-04 12:40:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 730640db-52cd-355a-9c5c-43ff852198c2 | -10.9855 | -49.7562 | 2025-09-04 12:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 157.5 |
| 665ed1c1-1f5f-3894-9448-0d6906c04f80 | -6.3689 | -45.6483 | 2025-09-04 12:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 45a14687-78df-3a06-bcaf-3dc479feb433 | -7.7409 | -48.7772 | 2025-09-04 12:40:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 101.7 |
| b7b93389-1a63-3a7e-ae2d-39af9e88d87c | -6.2205 | -43.5558 | 2025-09-04 12:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 8ca4bb88-970f-346f-b77d-d35bc21ca490 | -6.2318 | -42.4278 | 2025-09-04 12:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 127.9 |
| 36cb15e0-bc0f-35a2-b2b2-29db3b9c3f36 | -7.6854 | -48.717 | 2025-09-04 12:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 127.5 |
| 05149c5a-ae99-3b04-8d84-e36584e84d44 | -17.0652 | -46.449 | 2025-09-04 12:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 171.6 |
| 5dc5d45c-6324-3d60-acc5-3fb6af3c62d6 | -4.9951 | -56.256 | 2025-09-04 12:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 0be83998-90f9-3063-b4c3-616f00f57049 | -13.8651 | -47.9734 | 2025-09-04 12:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 65a9f25c-b862-3e7a-a159-47baeeffb1ac | -22.6558 | -43.7079 | 2025-09-04 12:40:00 | GOES-19 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 122.4 |
| e3cfa38b-f0bc-3116-b01a-0cc8c145f2dd | -7.6851 | -48.7386 | 2025-09-04 12:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 196.2 |
| c875928e-cad8-303e-b078-91b0cac9d1bb | -11.5779 | -52.115 | 2025-09-04 12:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 87.8 |
| f3c4d8aa-3171-367d-ace8-51f8db5249cb | -10.6769 | -51.5767 | 2025-09-04 12:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 839f8301-e601-3744-815d-aecf3c7cd872 | -5.6963 | -45.6076 | 2025-09-04 12:40:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| f4fd7c18-922b-3d6f-9d00-3cc95c77e18f | -9.7108 | -48.9636 | 2025-09-04 12:40:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 76c8878f-779e-3dd4-b79f-7100f3d1a87b | -8.3641 | -48.3334 | 2025-09-04 12:40:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 8e2c9aff-46df-36b4-9fc9-e1c9e638b5ee | -11.0062 | -45.9072 | 2025-09-04 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| e3b0701f-6a4c-35f6-bd64-160b16787dad | -9.6919 | -48.9655 | 2025-09-04 12:40:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 29398cee-e89e-3484-879f-d7ce024d7748 | -4.9049 | -41.7696 | 2025-09-04 12:40:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 205.1 |
| 7eb12ccc-b8ed-37c4-8cce-710087ff1d17 | -7.7039 | -48.7371 | 2025-09-04 12:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 50dc610a-752b-32d3-b4e7-aac11c52b108 | -7.7036 | -48.7587 | 2025-09-04 12:40:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 2851399d-4d91-37bd-bc04-3a878dee21e2 | -8.3829 | -48.3317 | 2025-09-04 12:40:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 7985c3cf-d55f-389e-94dc-1a77249416d4 | -6.2315 | -42.4515 | 2025-09-04 12:40:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 190.2 |
| b3ce3eaf-390b-364f-8964-47842a80380e | -11.853 | -51.453 | 2025-09-04 12:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 30451b57-6b2d-3963-b089-a9f027d105a4 | -7.6849 | -48.7602 | 2025-09-04 12:40:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 6c184375-f635-34eb-8f47-4b0f2ebd4aef | -5.7 | -45.1786 | 2025-09-04 12:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 5325e792-c93d-3f8f-a4c8-33e3f017358b | -8.0799 | -45.339 | 2025-09-04 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 6b17e04f-a29f-3bb2-9b1c-f53534850881 | -12.4593 | -48.0885 | 2025-09-04 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| ef898670-7f81-3791-a645-31b2d0eda37f | -8.3644 | -48.3116 | 2025-09-04 12:40:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| ff4de038-584a-31d3-ad23-40e935292af0 | -6.8754 | -45.5625 | 2025-09-04 12:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 5735286e-4bce-3cc3-afbf-99b79aa3d5b4 | -14.9865 | -50.0769 | 2025-09-04 12:40:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 881074a1-a47b-3ecb-ac7c-e071b08771f0 | -8.9031 | -45.82 | 2025-09-04 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 47d0cb88-dbd7-3b0c-a934-4e7e63620fe3 | -10.4658 | -50.3907 | 2025-09-04 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 126.3 |
| abca3ee8-3287-398d-9f0e-f6616c9ca8cf | -8.3829 | -48.3317 | 2025-09-04 12:50:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 3a869949-50da-388b-a78b-9ddb851ad8ef | -8.0799 | -45.339 | 2025-09-04 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 143.7 |
| b58ec032-1132-38a8-a720-ff0c1e6290e5 | -11.6231 | -46.6614 | 2025-09-04 12:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| c2e672ed-494e-38e0-8e1e-aa9904c0f09b | -6.8941 | -45.5609 | 2025-09-04 12:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 06973511-37de-3f0f-9571-53bf55816078 | -5.908 | -57.7311 | 2025-09-04 12:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| c01d6876-76b6-311d-940d-f1afe8738134 | -4.9049 | -41.7696 | 2025-09-04 12:50:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 122.4 |
| 8df008f4-753e-3eb6-abec-1d723178aeee | -11.0062 | -45.9072 | 2025-09-04 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| d774333b-c56b-3f54-8812-8a11df9e0a81 | -7.6851 | -48.7386 | 2025-09-04 12:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 209.8 |
| 2a857c4c-dbc5-367a-8019-68424c6e2e4d | -9.7108 | -48.9636 | 2025-09-04 12:50:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 177.0 |
| c84a4330-f355-3e35-a762-00a5793a0029 | -11.6601 | -54.5093 | 2025-09-04 12:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 21b8edc8-3fe8-30a3-baf5-5e0a9e1fac1f | -7.6854 | -48.717 | 2025-09-04 12:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 114.1 |
| 41514a54-120e-3b90-835f-d491050cd22f | -9.3014 | -47.0986 | 2025-09-04 12:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 5739c3df-5fac-33bc-b021-2bde6ec9d558 | -8.3644 | -48.3116 | 2025-09-04 12:50:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 414a131b-3bed-3847-a06f-20f4094e1235 | -5.6777 | -45.6089 | 2025-09-04 12:50:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 293.2 |
| 87122736-6cfc-32fb-9e5d-a0665094bbd9 | -7.7039 | -48.7371 | 2025-09-04 12:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 117.1 |
| ef0324d2-ca45-3c32-aa06-d725b9f14020 | -6.2315 | -42.4515 | 2025-09-04 12:50:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 106.4 |
| 4b6f7ff8-59b6-3036-b8bc-f32b886d4043 | -9.7111 | -48.9419 | 2025-09-04 12:50:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 1491ec10-edef-367c-8366-c1cf96cda165 | -7.0502 | -43.2724 | 2025-09-04 12:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.5 |
| a71eaf30-116d-331e-b74a-2f05481da3ae | -5.7002 | -45.156 | 2025-09-04 12:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 38551e5a-0913-3e2e-bb5c-0fb32e5a2c9f | -7.7036 | -48.7587 | 2025-09-04 12:50:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 155.6 |
| f8384f44-fef3-32b7-8b0e-65d39cba4cde | -5.7 | -45.1786 | 2025-09-04 12:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 48b057a4-126b-380d-926a-0c738f1a087d | -6.0232 | -46.6784 | 2025-09-04 12:50:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 33111b24-2efb-39e5-9d22-8566ad23e9ae | -13.8457 | -47.9764 | 2025-09-04 12:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 92e853ed-3662-3de8-9651-61607cc44546 | -8.0796 | -45.3617 | 2025-09-04 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 2fe6d019-29e9-3b68-b653-24c48bfd148a | -11.5779 | -52.115 | 2025-09-04 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 291cd837-f09e-3e3f-ac37-eeeb5c1afde1 | -7.6849 | -48.7602 | 2025-09-04 12:50:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 6dcbabd2-6da6-3061-afc6-acbf0b1561e2 | -8.3641 | -48.3334 | 2025-09-04 12:50:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 92dd880a-c684-3e0c-94d6-9be3919daeac | -11.5782 | -52.094 | 2025-09-04 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 40eca2c2-182c-3c98-8d25-3d0a2588bf23 | -5.6963 | -45.6076 | 2025-09-04 12:50:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 273.1 |
| 5448b490-4afe-3f1d-83e0-42beb70de906 | -13.8651 | -47.9734 | 2025-09-04 12:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 1405232c-67ee-3d18-9ca1-750b066fbc0d | -6.2318 | -42.4278 | 2025-09-04 12:50:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 104.3 |
| 8b5b731f-72a9-329e-b303-7b200c610662 | -17.0652 | -46.449 | 2025-09-04 12:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 154.4 |
| 0b19f04f-9bb4-3f37-bb5d-05048d5adfdd | -11.6599 | -54.5297 | 2025-09-04 12:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| a7728c0e-e0e1-32f7-8692-476acfd7f924 | -12.4593 | -48.0885 | 2025-09-04 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 8223a8b8-5b31-3211-815f-33dffdbe02dd | -9.7105 | -48.9853 | 2025-09-04 12:50:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| cd046268-810a-318c-919e-76cb17f1a569 | -6.8512 | -44.2886 | 2025-09-04 12:50:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 15f1f075-f61b-36fb-95c6-e263caf5f17b | -10.6769 | -51.5767 | 2025-09-04 12:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| aa028655-8409-3e9c-b01c-b03d42c0e695 | -12.2344 | -50.1488 | 2025-09-04 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| b32972c6-8283-390c-978f-f5ae77b55ede | -11.0062 | -45.9072 | 2025-09-04 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.2 |
| fd9bcd34-2962-38dd-83d9-acf1a137d752 | -6.0232 | -46.6784 | 2025-09-04 13:00:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 9ea2ba6f-9361-362e-bafc-239e96bf00e1 | -6.8754 | -45.5625 | 2025-09-04 13:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 962c2837-ab9b-3146-a044-e1be24fd676c | -7.6854 | -48.717 | 2025-09-04 13:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 119a4d08-17a0-3854-94e5-086e36b086a7 | -7.7039 | -48.7371 | 2025-09-04 13:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 279f4ea3-c2be-35b3-8e5f-f036f3e574d9 | -7.0502 | -43.2724 | 2025-09-04 13:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.4 |
| 7ba5862e-a877-3884-83d2-dfcea4592359 | -5.7002 | -45.156 | 2025-09-04 13:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| e0d50d56-822b-390d-bdbd-4882d506547f | -13.8651 | -47.9734 | 2025-09-04 13:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 6dc457d8-57c7-3722-9538-78a5ce324632 | -8.3644 | -48.3116 | 2025-09-04 13:00:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| d2cdb4c9-bdbd-3e83-bc6a-a910a6d4c107 | -6.2318 | -42.4278 | 2025-09-04 13:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 116.3 |
| c79631c0-23fd-3334-955d-408661939c2c | -5.908 | -57.7311 | 2025-09-04 13:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 46250767-cdda-3dd7-809b-f9481ff9f114 | -8.3829 | -48.3317 | 2025-09-04 13:00:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| ca2c5b73-859d-3456-ba96-fd415b60b7d2 | -8.3641 | -48.3334 | 2025-09-04 13:00:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 103.0 |
| ca2f59f0-9da2-319c-a20b-164339d07fbc | -10.4658 | -50.3907 | 2025-09-04 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 150.4 |
| 0223153c-05c5-3846-9ce6-d5e531eeeb9d | -6.1665 | -43.3273 | 2025-09-04 13:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| d6b4e88d-370e-311a-86d5-153fe6305e06 | -11.5782 | -52.094 | 2025-09-04 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 0d9484cb-a63d-3eae-b32b-5cf5ddf919d7 | -8.0799 | -45.339 | 2025-09-04 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 139.0 |
| ea89693d-e348-377d-9104-903ef5b66a13 | -11.6601 | -54.5093 | 2025-09-04 13:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 325a651b-e89e-328b-8076-f49ba5afd17d | -5.7 | -45.1786 | 2025-09-04 13:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 164.0 |
| 5ab4824b-c1bb-39bd-8b32-9af0a2b3481f | -7.6849 | -48.7602 | 2025-09-04 13:00:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 95.9 |
| c37f762a-ccf2-35cc-ab8d-7761452fc855 | -11.6231 | -46.6614 | 2025-09-04 13:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| c742558f-2ce0-3abe-8959-4ddb31fad19c | -11.7389 | -47.7415 | 2025-09-04 13:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 87e421f7-a917-3c67-89c2-6a20e16f018a | -6.8941 | -45.5609 | 2025-09-04 13:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |


[Clique aqui para ver as próximas entradas](README104.md)
