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

## Dados Diários - Página 411

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64729b56-7147-353c-8c46-a8fc1586db4f | -6.895 | -43.7066 | 2026-10-08 19:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 95.1 |
| ec1658ac-c2de-34ad-a6e9-a05ddbf52fe0 | -5.7922 | -43.2405 | 2026-10-08 19:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 2c6f9016-6b7c-39e8-8008-05733ffa1a48 | -6.1429 | -47.9432 | 2026-10-08 19:40:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| bba3f508-2091-3ba9-9d6e-80665ff350f2 | -1.3111 | -54.1982 | 2026-10-08 19:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| b6aad628-85b1-3be1-879f-cfea17a69b09 | -9.9011 | -44.8378 | 2026-10-08 19:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 17443d3a-5951-33ef-b37c-079e32c2fc9a | -9.0362 | -44.3654 | 2026-10-08 19:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| f5054b98-0fc6-3341-905d-9bdc8385d320 | -2.5171 | -56.1459 | 2026-10-08 19:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 20c88808-d25c-371c-8d7f-14f114d5649a | -6.6027 | -37.8944 | 2026-10-08 19:40:00 | GOES-19 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 106.4 |
| a1d7537e-6028-3221-ac73-ab9d7d68973b | -2.6262 | -56.4778 | 2026-10-08 19:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 100.2 |
| e1eb212b-4cff-3c6c-8e97-a64b4de1fa97 | -5.9833 | -40.961 | 2026-10-08 19:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 200.1 |
| 78502725-11e2-329a-9d23-82234f9003c2 | -9.017 | -44.3907 | 2026-10-08 19:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 8077b51a-07e9-357a-bf4b-8f778008d6b3 | -6.1042 | -55.6964 | 2026-10-08 19:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 127.2 |
| c92b96e8-ebeb-3033-8352-1e61bf90e006 | -3.7057 | -57.0998 | 2026-10-08 19:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 89d346f2-0349-35a1-ab72-cb03e043d7c6 | -6.9328 | -43.6799 | 2026-10-08 19:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 2516f889-9ccc-3dbe-9c15-b9c022df1bd5 | -2.8256 | -51.2779 | 2026-10-08 19:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 145.7 |
| e713dad8-3763-3753-b1f2-102934611606 | -2.9979 | -54.7692 | 2026-10-08 19:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 6144b109-181e-3102-948a-e4e960ef1ad2 | -5.977 | -55.3639 | 2026-10-08 19:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 13c19c51-7079-3919-b4f8-a5ba6571d1be | -2.4987 | -56.1659 | 2026-10-08 19:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 115.3 |
| 6d2834a9-6125-33b1-9e99-5db8ce37672a | -6.1501 | -51.6992 | 2026-10-08 19:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| b3112954-e6e9-3fa7-b8ca-e166454443c6 | -6.0024 | -40.935 | 2026-10-08 19:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 99.2 |
| dffdd28e-926c-38a4-83e1-bc18dc0f87bb | -7.0706 | -52.6764 | 2026-10-08 19:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 085c9215-653a-3801-be39-07df51dcbf77 | -1.1094 | -54.1802 | 2026-10-08 19:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 79d74a32-5218-33cd-980c-eb3e0524dfe3 | -8.0764 | -45.6339 | 2026-10-08 19:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| ff01dd9c-1f4d-33e1-b5b3-edd8fa75b973 | -3.1114 | -53.8041 | 2026-10-08 19:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| cf8b6ef9-76cf-370b-8e82-428c677805b2 | -2.7428 | -54.1347 | 2026-10-08 19:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 130.9 |
| e7868380-d71d-3c42-857e-5a9b79692924 | -2.4987 | -56.1856 | 2026-10-08 19:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 8972c975-6584-3ccc-bcc2-ccf282aaeddc | -2.8895 | -54.1915 | 2026-10-08 19:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| e19e4815-7ff2-3586-b40f-15bdcd4f206c | -12.2311 | -44.7661 | 2026-10-08 19:40:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 169.7 |
| 3143004e-e990-3dfc-ac1d-26538f0745d7 | -6.2155 | -52.8899 | 2026-10-08 19:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 145.3 |
| dd92eb13-d762-3909-976e-e29847b037f7 | -5.1133 | -46.2048 | 2026-10-08 19:40:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 9a78234b-c4b7-328a-96f9-ed83268603a8 | -3.095 | -59.1832 | 2026-10-08 19:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 9f339681-a896-3391-80f4-41b02aeeb424 | -2.5491 | -58.0566 | 2026-10-08 19:40:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 8907bcbc-60c3-32b3-8a9b-617ae0d0d7c9 | -6.4032 | -55.1842 | 2026-10-08 19:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 5b288989-2586-39a9-8bfe-21769847baf8 | -4.6364 | -50.9437 | 2026-10-08 19:40:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 362.9 |
| 7285942b-5a70-39ec-9c42-e55a4bb34985 | -2.77 | -57.5293 | 2026-10-08 19:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 117.6 |
| 93395ec4-9214-38d9-9f3e-1ec2e00183ed | -3.9299 | -56.034 | 2026-10-08 19:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 172.2 |
| 650e5e09-53f4-360e-a068-7d94ed85b6ba | -1.1094 | -54.1601 | 2026-10-08 19:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 7e9df021-eee6-3296-9945-c20a099389bc | -3.0163 | -54.7488 | 2026-10-08 19:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 02dd018d-a45d-38ed-9105-a3fb53a3aba1 | -4.0837 | -44.1389 | 2026-10-08 19:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| c587921e-8f73-3f41-9503-4fe99680859f | -6.1977 | -52.7886 | 2026-10-08 19:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 130.9 |
| a15adf72-b643-36cb-ae66-b55ab048cae0 | -3.86 | -44.1274 | 2026-10-08 19:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 8ba9269b-a8e9-393c-a923-b847d7ca0dad | -6.4413 | -55.0224 | 2026-10-08 19:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 120.9 |
| 7385f72e-6a9c-3826-8442-d40796c1eaf9 | -8.9772 | -45.9249 | 2026-10-08 19:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 6e4f06b7-b56e-3e3d-b753-09af0df7ca5e | -5.5146 | -42.8399 | 2026-10-08 19:40:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 92.7 |
| d20e5335-3298-3e24-a8b0-d46774e4db7c | -5.3763 | -45.943 | 2026-10-08 19:40:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 30655718-2f2a-3648-8be7-7270a855a3a1 | -2.5492 | -58.0373 | 2026-10-08 19:40:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 146.6 |
| 20a01c07-2483-3d38-aada-1b83fe964e25 | -7.0892 | -52.6753 | 2026-10-08 19:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 235.7 |
| d133fd56-cef4-3106-881b-a2e84e9da133 | -6.8904 | -45.9212 | 2026-10-08 19:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 6f8cd6ac-94e5-3f2f-b741-32d05bffd74e | -6.1227 | -55.6955 | 2026-10-08 19:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 151.7 |
| 480e5076-839a-3e63-ae09-811e666dcaac | -3.8413 | -44.1283 | 2026-10-08 19:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 2d626df9-c0d9-3fe7-969c-dfdcb921b028 | -2.7429 | -54.0945 | 2026-10-08 19:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 129.6 |
| 5e48da89-aacb-3e0a-81fa-1732c4d78f44 | -3.2956 | -53.6984 | 2026-10-08 19:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 2764317c-649b-3556-a74b-50254f45d4bd | -2.899 | -57.196 | 2026-10-08 19:40:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 9573d87d-32ea-3133-b5b7-132eac8adf59 | -11.7738 | -43.5482 | 2026-10-08 19:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.9 |
| cc0e267d-170d-3627-b6c2-654815c99bb5 | -6.2162 | -52.7876 | 2026-10-08 19:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 204.4 |
| adb0fdf0-54e5-3f21-8422-51e1fa3d5c37 | -11.6387 | -43.5929 | 2026-10-08 19:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 42e1897b-7692-323f-a8ee-5aa13b51ab7a | -15.1051 | -43.6409 | 2026-10-08 19:40:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 152.6 |
| 7d409ddd-e7e9-34e7-991d-512b58d01325 | -9.5004 | -66.7831 | 2026-10-08 19:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 6f24e829-cc82-3faa-ba66-66c6811ac63b | -3.2717 | -50.3893 | 2026-10-08 19:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| bebad71d-c5fa-37cd-83be-e20067f7f40d | -14.6529 | -41.2684 | 2026-10-08 19:40:00 | GOES-19 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 91.1 |
| b9e16d8b-8ad4-353d-b605-8d62334fcb77 | -1.3264 | -56.398 | 2026-10-08 19:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| fe945729-e9e0-3a96-b381-5bfde5465bbf | -3.2081 | -58.0057 | 2026-10-08 19:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 397.2 |


