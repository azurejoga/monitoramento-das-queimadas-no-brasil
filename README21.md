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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7577523-b288-30f6-b84d-cd32af9eccb5 | -6.64488 | -56.41883 | 2026-08-08 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89119ca1-0b78-3109-b1d5-4cb12df5b6a9 | -8.68459 | -62.87038 | 2026-08-08 05:29:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8592abc1-01b2-32a1-be2c-8a7c37761413 | -4.37071 | -55.77277 | 2026-08-08 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a13c0177-f899-354b-9fb7-e2162a8dc9ec | -8.14606 | -55.42088 | 2026-08-08 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| a4640126-f81e-3663-b57e-584a9a88d960 | -8.6912 | -62.87142 | 2026-08-08 05:29:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7d04197-f6b2-322b-9f91-533c74674223 | -3.39248 | -59.4418 | 2026-08-08 05:29:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38f62e31-726c-341d-b2b5-46ab9f4ea1a7 | -8.68128 | -62.86986 | 2026-08-08 05:29:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cfee3186-94e8-3733-9f7f-188cb72ed2a9 | -6.84287 | -58.979 | 2026-08-08 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0c98c590-7bf0-3f7e-9113-eb4db6cc8ca0 | -7.74603 | -56.33204 | 2026-08-08 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b132f1c7-e58e-3ad7-abaa-6913a50ad925 | -7.8464 | -56.59083 | 2026-08-08 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b37ad6e-bc34-3d18-9f7d-bda3d84ee2d7 | -6.89153 | -59.90018 | 2026-08-08 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85c50186-a95d-3377-a511-2576414ce1ce | -8.68844 | -62.86742 | 2026-08-08 05:29:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d74dfcc-c5ef-383d-8d85-3bc093991fa0 | -8.6879 | -62.8709 | 2026-08-08 05:29:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa358e4a-26e7-34c7-a97f-3bde7f0e2e06 | -3.99992 | -56.23843 | 2026-08-08 05:29:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16bfe34b-7a06-3a55-afb2-cbf12d79ad9a | -8.35847 | -63.7526 | 2026-08-08 05:29:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c79da45e-23c8-3e2d-9e68-7f207c380f5c | -6.84778 | -58.97109 | 2026-08-08 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb1779a9-b512-3bb3-b65b-cf5db5f90d65 | -3.83894 | -59.29881 | 2026-08-08 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 939de19b-c85f-35d6-88fc-8eefcaac050e | -6.89211 | -59.89633 | 2026-08-08 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2d72d546-934f-3fd1-a59a-9454e0134b24 | -4.00203 | -56.23592 | 2026-08-08 05:29:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25f53502-74be-3cea-a18c-ea747e54e125 | -4.36642 | -55.77214 | 2026-08-08 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d289be98-7508-3e1a-a3ff-0a51618bda4c | -6.85774 | -58.9578 | 2026-08-08 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 785ab1e7-4018-31c1-85a9-24c2b988b655 | -3.11833 | -59.92856 | 2026-08-08 05:29:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32ddd333-7bb9-3b00-89bc-9bed7cb92029 | -6.72342 | -58.92758 | 2026-08-08 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c6168288-060e-3067-87dc-32caa1a6fad1 | -8.68183 | -62.86638 | 2026-08-08 05:29:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9dad9dac-21ce-3d02-8818-50e0ffba47f2 | -6.28264 | -64.15314 | 2026-08-08 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e5ac7a4-970f-3c09-a4e6-deb8061a9a5d | -7.74662 | -56.32792 | 2026-08-08 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 872f0589-f68a-3fec-8f01-c020a34210c0 | -4.93244 | -62.332 | 2026-08-08 05:29:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 09759319-7f67-3354-846a-71d2916c2015 | -7.55601 | -61.15514 | 2026-08-08 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1c7e097-5210-35e0-b913-65d277e0a3ba | -7.55546 | -61.1587 | 2026-08-08 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ca589dc8-2ba6-3862-831c-032c2e335dbd | -6.70932 | -58.94714 | 2026-08-08 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| da8bc4e3-cbda-39db-b79b-b827365cee3c | -6.96291 | -60.14537 | 2026-08-08 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f058a0cd-eec7-3d7b-ae8b-84bb74aa9f6a | -6.70869 | -58.95139 | 2026-08-08 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4518051a-48a2-30a3-9448-c1c2b106297a | -6.96003 | -60.14106 | 2026-08-08 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7294fce0-0651-36c0-82c7-4227a62ab6ba | -7.5521 | -61.15819 | 2026-08-08 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a3f4cdc7-21bc-300f-96a0-673695948d51 | -6.71169 | -58.95614 | 2026-08-08 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 666f9e5f-e382-3e17-8c2a-29651b0d72e2 | -6.86877 | -58.93335 | 2026-08-08 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27ba2b40-6f58-327f-9fb5-61a0fdf5663a | -6.64543 | -56.41505 | 2026-08-08 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58992270-61c4-370d-afa8-676e71f129fe | -4.92967 | -62.32804 | 2026-08-08 05:29:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73a0faf7-1df3-3b89-b160-3345cc7a4577 | -6.72215 | -58.93604 | 2026-08-08 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7e89e758-d1af-31b5-b351-58f27f42739e | -5.8837 | -57.64912 | 2026-08-08 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 20ac6764-e6b4-3041-95c0-38ee3482922e | -8.16023 | -61.5143 | 2026-08-08 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b06550a-4bd8-3568-a45d-23cea2788136 | -6.60546 | -56.36051 | 2026-08-08 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02d81199-bb43-3d99-9fe2-2cb53718d630 | -4.2634 | -48.2016 | 2026-08-08 05:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| a91d0a39-22be-3d39-9aa2-0d9f137e3fb4 | -15.15932 | -52.73777 | 2026-08-08 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b532f7e-8af6-3bea-910e-73236aa87f28 | -15.37838 | -53.79866 | 2026-08-08 05:31:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2d9ae239-1814-36e3-9e96-e4ad139bff2e | -15.16583 | -52.73884 | 2026-08-08 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b7a0f809-5ce6-372e-839b-90928354bbdd | -10.94397 | -68.74741 | 2026-08-08 05:31:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f71a5510-533c-3389-a356-07982590a372 | -14.32879 | -54.94479 | 2026-08-08 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2949e03f-24e3-3c05-9a9d-3aa2b08b60b5 | -14.16819 | -54.00377 | 2026-08-08 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a8cd8340-7416-3069-8a7a-a08b283ef282 | -11.19522 | -54.84532 | 2026-08-08 05:31:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e6bb92e-6280-3598-96f4-1eea121ff7d8 | -14.31227 | -54.9955 | 2026-08-08 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 5b6435c0-f5a5-3e53-b02b-cd1166080134 | -15.16492 | -52.74782 | 2026-08-08 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e1bcc283-d7da-3938-ad64-6f8c9e13fd85 | -15.16545 | -52.73826 | 2026-08-08 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 231e0d38-d453-3bf8-a701-b7cb5cb12275 | -15.38092 | -53.79202 | 2026-08-08 05:31:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b39bf059-5278-37ea-adb5-cb2c3ae85d20 | -15.38456 | -53.7954 | 2026-08-08 05:31:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 29dd33c8-3d5f-37aa-b972-aa3d9df406a5 | -11.19674 | -54.83992 | 2026-08-08 05:31:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4778ec76-4685-35a8-b93e-f4f96a9db1ed | -8.78774 | -64.21524 | 2026-08-08 05:31:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9f8cda7-435f-3d7f-8c38-b78aaab047b1 | -12.3291 | -53.16161 | 2026-08-08 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3e83f89-7df5-34b7-985b-80ae9bdcb06a | -15.39637 | -53.81051 | 2026-08-08 05:31:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6c33ed1c-227d-33ed-aa71-b2dff6274cc0 | -8.78832 | -64.21162 | 2026-08-08 05:31:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3302543-fcee-345a-9c18-6e2ef590f5aa | -14.36282 | -54.97209 | 2026-08-08 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54d29924-c0a8-3bf5-92c2-bd337c922d4a | -11.24302 | -54.02 | 2026-08-08 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 78226777-880a-329d-b832-8d0a9eefcb6e | -8.78495 | -64.21108 | 2026-08-08 05:31:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 96ed7121-00a5-357b-a0b4-62b73cc152c4 | -12.33533 | -53.15831 | 2026-08-08 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e16d19d0-edd7-3f73-bc34-bb29129891c4 | -14.32946 | -54.98465 | 2026-08-08 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7884d6b1-10d0-3bb5-a3fe-0b35ce5e97a8 | -11.83874 | -56.94276 | 2026-08-08 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9bec23c6-68dc-31ee-b71e-be1c459c70a2 | -14.30705 | -54.99482 | 2026-08-08 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d35042b-8e40-3fbc-8357-0c439cbbaf73 | -11.02042 | -50.53471 | 2026-08-08 05:31:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 14ccb612-30e1-3113-9ad7-37a631ba6454 | -11.72915 | -62.32681 | 2026-08-08 05:31:00 | NOAA-21 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bcf5ffea-21a8-373b-9760-7a5f0890b438 | -14.33433 | -54.9884 | 2026-08-08 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b4b9b00-3985-38e1-9a77-ba3c493733a6 | -11.19559 | -54.84228 | 2026-08-08 05:31:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21a6137b-d1ad-3e06-9439-77ada6ee547a | -14.32348 | -54.99041 | 2026-08-08 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 19134b29-b5ce-372e-9b01-e8b0f50b8afb | -14.30742 | -54.99158 | 2026-08-08 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 999ff2f4-1f87-35b8-af14-722cf55ac80f | -8.8506 | -63.54494 | 2026-08-08 05:31:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 574bb679-bd0e-36f9-a1c2-2a06f1727d6b | -14.36985 | -54.91296 | 2026-08-08 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9d92366a-acff-3d83-8029-3af99a35f263 | -8.85393 | -63.54547 | 2026-08-08 05:31:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a66436c1-47e4-3ab9-a836-1836d6f48828 | -15.38049 | -53.79604 | 2026-08-08 05:31:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 95f2d332-67eb-3e25-8823-2b9a97dc0aaf | -10.9458 | -68.74795 | 2026-08-08 05:31:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b48b43ef-b57e-3b98-8243-c7eec837ec74 | -9.84474 | -56.07545 | 2026-08-08 05:31:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bc6ab933-51a8-34ac-a072-4d981e534754 | -11.19595 | -54.84598 | 2026-08-08 05:31:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba0cc621-fb43-34a1-9246-9552e9c30afd | -11.1544 | -54.8491 | 2026-08-08 05:31:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e986c2a6-54d7-391f-8aeb-fc0913af0564 | -11.6132 | -54.64912 | 2026-08-08 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e451f02f-6135-399b-9225-a48dbd490578 | -15.3968 | -53.80651 | 2026-08-08 05:31:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5a920702-6baa-362f-be1e-526942f73dd2 | -11.01377 | -50.53384 | 2026-08-08 05:31:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 90781650-d468-377d-968e-162abb9ac361 | -10.82324 | -65.09648 | 2026-08-08 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7047f185-0610-3997-b307-ac8f23205225 | -8.57628 | -63.86029 | 2026-08-08 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 185e568d-5bb2-39a7-9fd9-3c9075ddd0aa | -15.15275 | -52.74134 | 2026-08-08 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 40f4927f-966b-37a1-8d41-271aa97f69c4 | -15.15363 | -52.73713 | 2026-08-08 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bed5872e-9ae9-3642-ba7c-102cc15c4903 | -14.16215 | -54.00722 | 2026-08-08 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4358b8aa-1e58-3360-b3cd-6c48d5771918 | -11.24837 | -54.02065 | 2026-08-08 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 43838e64-c334-35f9-84aa-104a3be3c5dd | -14.32918 | -54.94146 | 2026-08-08 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f54e9ff1-09d4-3459-b441-bf117bc7aa5b | -11.73194 | -62.33092 | 2026-08-08 05:31:00 | NOAA-21 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fc76dbc-1b9d-322c-9e45-ecc2ea1c4e96 | -14.16696 | -54.00549 | 2026-08-08 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 61e656ef-d487-3aa7-aedb-29ec5e5102f2 | -15.15969 | -52.73844 | 2026-08-08 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 22e8c9e9-aa4d-3dd5-9d6a-94a7ce5da20e | -9.74908 | -62.36475 | 2026-08-08 05:31:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9b7ebd2d-2ded-3b6c-ad02-2094058a69cf | -11.61281 | -54.65228 | 2026-08-08 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 992e27b6-bea3-386b-a58a-1efa52bde7c7 | -15.70313 | -54.85324 | 2026-08-08 05:31:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f63147ed-1a72-340e-b254-5bcfc2b636d8 | -15.15327 | -52.73646 | 2026-08-08 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c650e39c-2e7b-3b0e-a017-27a629a34674 | -15.16536 | -52.74345 | 2026-08-08 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e891a87b-4d93-38d5-9eef-b8af672e60ca | -14.1674 | -54.00149 | 2026-08-08 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README22.md)
