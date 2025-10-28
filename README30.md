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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 393376db-6374-33c7-9f74-e55a7a826131 | -7.27647 | -44.97289 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ddd243c3-3897-319d-a3d5-0719cf306e02 | -6.18292 | -44.8683 | 2025-10-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 145f7002-441c-3adf-ab75-4fe73ac37d9a | -11.02552 | -44.64694 | 2025-10-28 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cf261e45-13d2-3baf-81a4-0992f46e1628 | -8.45386 | -45.12385 | 2025-10-28 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a543bd1-99d0-3155-af69-455426867b12 | -12.52979 | -47.55354 | 2025-10-28 04:14:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc1cec17-e905-35a4-b983-7630cd03ad40 | -10.29234 | -47.20337 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9d1c9019-3528-3781-bffa-caeb303af2ca | -10.33535 | -47.77966 | 2025-10-28 04:14:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5e3d56c0-56c6-39ab-9dae-c436f19ee66d | -8.12063 | -45.48929 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d380e43b-031a-3028-b4d4-02c631b194ac | -7.5097 | -46.74694 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c5a77a9-348a-305f-8801-c283a28bf260 | -8.25876 | -46.89571 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 7097249a-475a-3000-8c9e-025fe86f8571 | -7.85444 | -47.09784 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1cfc422b-1522-3e21-bddc-d4bfc5eeac61 | -9.11057 | -48.6986 | 2025-10-28 04:14:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d1b92f13-8d0c-3c48-a38f-3d135ffcb2e4 | -12.21759 | -46.48941 | 2025-10-28 04:14:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e29aa260-a436-3b18-af77-d1827354cb33 | -7.60199 | -43.58958 | 2025-10-28 04:14:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6891d1f3-ca8f-372b-9e35-e9be7e9faedb | -7.96659 | -46.75446 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| d04840f7-95ce-3ba3-bc4a-b6f40a53243f | -6.24309 | -42.55366 | 2025-10-28 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bfe053b8-a809-3b6d-b498-ec97926c5e17 | -7.86764 | -46.38971 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 47d98198-487c-36de-87e0-043986cebbb6 | -6.98944 | -43.99842 | 2025-10-28 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f0ae7f0-8baf-35ad-9d53-d64256700e09 | -7.89373 | -45.69528 | 2025-10-28 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 535d4dbd-00fe-3791-a84f-a5555c95403b | -10.96532 | -44.85406 | 2025-10-28 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 58df39c1-15c2-33f2-8cc8-e2a5c1b94117 | -7.95017 | -45.50111 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 71a68cb1-6bab-325e-8001-dd0e82149d61 | -6.42649 | -42.02988 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0d7c78a4-483f-3317-a17b-f3f510f2fa97 | -12.22663 | -47.92353 | 2025-10-28 04:14:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d0899610-07b3-3f54-aad6-d8d13da657d3 | -6.82227 | -41.20892 | 2025-10-28 04:14:00 | NOAA-21 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 59550389-fffa-3f32-9278-49207c8a9b2a | -7.00492 | -47.00127 | 2025-10-28 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b2cec36a-ff39-3dab-a204-ab3ba8f8bbd5 | -10.22644 | -49.90089 | 2025-10-28 04:14:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 313919f3-aa5d-33cc-8442-09616f8fe939 | -6.89349 | -44.90466 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 32caa903-f0e5-3892-abd7-2906086b7c6f | -11.71461 | -44.44283 | 2025-10-28 04:14:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3b1e02b-a8fb-38d6-9f35-b488eededac3 | -12.08837 | -45.66402 | 2025-10-28 04:14:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 88dae5a4-ba5f-3c10-aa90-035ebba3ed33 | -7.96654 | -45.53097 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b579228-457b-3c49-8489-67dafccfd51f | -6.16288 | -43.08815 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98ebcb38-e2ea-3058-8e70-830c794da923 | -9.95867 | -47.11111 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| ec91fa80-65a4-32b4-9391-36ca63aa39e8 | -6.24662 | -41.80705 | 2025-10-28 04:14:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 99f44699-845b-330c-94e6-d2a998548c37 | -9.76761 | -44.9986 | 2025-10-28 04:14:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0c2cc15e-2cd5-3f66-ad50-d18e332ac3a5 | -12.20749 | -46.50755 | 2025-10-28 04:14:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cbd4cd1a-9bd5-3aec-aae1-707654824045 | -6.12869 | -42.69763 | 2025-10-28 04:14:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e5b3a5be-dc4c-3342-9471-4c6fd1c098a7 | -8.09908 | -45.68518 | 2025-10-28 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6f9184a2-f5ab-3ea5-8236-2d41ed69fb51 | -7.15692 | -46.99621 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1ba9c6a5-1ed9-3ae7-bf47-8bc8e3db210e | -6.55562 | -41.60709 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 14d6d32e-fb56-3e5d-8375-97f209586276 | -6.83023 | -41.20255 | 2025-10-28 04:14:00 | NOAA-21 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 88ada63a-f471-3e5e-8101-9db6dd32e614 | -6.09998 | -44.68463 | 2025-10-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 40c641a1-e7b4-357e-9388-2e67e6a787e9 | -12.38728 | -42.48117 | 2025-10-28 04:14:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 47401f41-ead9-3724-bf0f-8d8fe6b97031 | -6.34581 | -44.61865 | 2025-10-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aee48ed9-c874-3868-a6b9-3405f88d7092 | -5.56598 | -51.0146 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4c2e26e-0108-3982-9600-99502bafe519 | -7.95644 | -45.50602 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f27c4377-398a-362b-9fc5-91cd3b9c595f | -6.68606 | -42.04545 | 2025-10-28 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 78ae2733-2810-33c0-ae26-62878d392c18 | -8.94853 | -44.9503 | 2025-10-28 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1f58a7a-7d80-319c-a7bd-e6e549dd1916 | -8.2002 | -46.93231 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7452f736-cfe7-33a1-96d2-3d10ac2902e5 | -10.94446 | -50.27115 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2306d4ab-aa98-3587-a473-3cffa46c66ff | -12.01178 | -46.75879 | 2025-10-28 04:14:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a6bcbe4e-7b39-3eb1-93f8-68e7a731abdc | -10.99095 | -50.36256 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f72ca6a8-529c-3921-a8d1-ee52d49a6ba6 | -7.98396 | -46.73983 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 45704826-9cf7-30bf-af16-0ecb9563836e | -9.54445 | -46.95926 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9513e21d-25d9-3329-b5d2-cafc6ae6a418 | -6.12288 | -42.45286 | 2025-10-28 04:14:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 12609c41-bff1-3153-9ee4-ed2a1fc57ceb | -7.26652 | -45.0131 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bc56ccc8-dd81-361a-8138-a9293fd61c26 | -10.76742 | -47.9001 | 2025-10-28 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9b5f9b0c-df39-3a72-9b09-bf1a296f0001 | -10.68374 | -44.35387 | 2025-10-28 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c62c5178-8076-364c-8f2e-ba44593aad85 | -6.18634 | -44.86884 | 2025-10-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd6ca089-612c-334b-8d34-053ec7687c48 | -7.86505 | -46.39747 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cc67e357-841a-3619-aed9-01b828c21c6b | -12.08143 | -46.39966 | 2025-10-28 04:14:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 71084a73-51f8-3572-9829-6d49cf21f52a | -10.57708 | -48.00911 | 2025-10-28 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bb70b084-4182-3237-9798-19b59cb4fd4f | -10.63472 | -42.31809 | 2025-10-28 04:14:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1dc1937e-bfd6-3cbd-ba7b-d275d5fb18a2 | -9.58849 | -47.85161 | 2025-10-28 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9adcd24-48f6-3183-9db5-72184979c2e2 | -7.9615 | -45.51843 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ce1bbb5b-8ca3-3897-9dd0-d28c6de523e6 | -10.68008 | -47.26895 | 2025-10-28 04:14:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 766cb9e4-11ac-3702-9fff-0dfe204bb682 | -13.37646 | -43.46053 | 2025-10-28 04:14:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7bd764a3-6614-3bd8-b120-be8e52290e89 | -9.24112 | -45.60299 | 2025-10-28 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50a3b199-bb4f-35ac-9b93-f0b3076941a5 | -8.16157 | -47.00682 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8d549955-ccc7-34d9-b2ad-145d3cb13105 | -9.97981 | -47.16304 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6f949c1a-f0d5-389a-a77e-d756d10bb1ff | -9.06176 | -46.9443 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 86e9218a-7511-3503-ae9d-60b6c3b8695e | -8.31753 | -46.8348 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8c840c5b-5dd2-3867-946f-1be2abb2494a | -6.69271 | -42.04648 | 2025-10-28 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c8ae361e-7124-38c2-a9ca-759f4fd17d0a | -6.69937 | -42.0475 | 2025-10-28 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 7d882965-dc4e-3f12-8446-de07162a3c60 | -7.4559 | -49.41027 | 2025-10-28 04:14:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| e66493ef-2ff2-36ba-8a00-dcf9f3728f25 | -9.23589 | -45.6136 | 2025-10-28 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 610de0e1-5699-3d12-bdc1-7275dc796fd9 | -9.71035 | -43.61853 | 2025-10-28 04:14:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2cce4c32-05f4-3ca2-9e94-295de6693c3d | -10.9074 | -48.01196 | 2025-10-28 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 486fa3b3-9c52-3bd4-9774-38dec93ed7ce | -9.47241 | -46.8707 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 550c7ef1-f76f-3729-9934-62d2cf2064a4 | -10.62851 | -42.31337 | 2025-10-28 04:14:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 363fe8a7-4272-3363-b8d6-31f171eee298 | -6.44383 | -42.35783 | 2025-10-28 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1d20f6e7-d44a-3d2c-bf2d-80cb20d38da4 | -6.64417 | -43.38344 | 2025-10-28 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6ec9e726-c530-3920-bf35-43b81347882f | -7.49256 | -47.03368 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 23718baa-2de7-3e08-88f0-45fd9d89c932 | -10.92434 | -50.2589 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0441c4e-73fd-31fb-be35-92a6c1108567 | -11.60345 | -48.53881 | 2025-10-28 04:14:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a212ad36-2c53-3369-8ffd-5596c7e70948 | -7.25577 | -46.81076 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99500a78-213c-3664-b229-0335c308591d | -11.64503 | -48.52625 | 2025-10-28 04:14:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c595ed1b-288a-326d-b92d-c93778f04021 | -10.29098 | -47.23388 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7727b4b4-e762-385c-a52b-55d06e30ec92 | -12.90098 | -46.80504 | 2025-10-28 04:14:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0bedaf28-8743-38ca-a306-67576e9f5ed1 | -10.306 | -47.1661 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| edfd3ea0-d0fe-3938-953d-e8a0706b96e0 | -10.6274 | -42.32071 | 2025-10-28 04:14:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 32752cab-8b6c-3d9c-ad63-e60f57312be8 | -8.70965 | -47.98473 | 2025-10-28 04:14:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 31ebc43e-d2c7-3a1b-b5af-a521d36edfe8 | -7.78796 | -46.44933 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e364e0d7-385a-388d-852b-42b6d662619c | -5.82778 | -53.45247 | 2025-10-28 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff07474d-ac51-3510-b255-59f4ed7296cb | -6.28545 | -44.70683 | 2025-10-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0245e835-7988-3190-93f7-9ac50dea209a | -8.85098 | -42.55889 | 2025-10-28 04:14:00 | NOAA-21 | CORONEL JOSÉ DIAS | PIAUÍ | Brasil | 2202851 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bcf79127-5fb1-3ba3-a576-1e3b58204199 | -10.93071 | -47.61065 | 2025-10-28 04:14:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bf6dda6c-e68a-3885-b90e-9c469191502f | -5.56675 | -51.01326 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8307718f-34ab-3b45-9b30-bcf4efdec3d1 | -7.94143 | -45.51141 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9e8d03ca-868b-3c9c-be7f-7f00b91c6cc2 | -7.94452 | -45.49241 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 52047b1a-641e-345a-8b3b-1b58eb3aacaf | -6.60843 | -44.64194 | 2025-10-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |


[Clique aqui para ver as próximas entradas](README31.md)
