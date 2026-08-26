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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cada7764-f393-30ed-940c-63d80c43376c | -6.99818 | -59.26549 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 65fa41cb-2233-3712-8332-9be56b2c456d | -7.38442 | -55.18035 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b83260e-d2be-3fc0-a6ae-5410ccb2b63b | -6.84359 | -59.43019 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3cd392cb-7e63-32bb-af8c-00f9f5273205 | -6.83905 | -59.45693 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2a19d1f-46da-32c8-b81e-4298099ffbac | -6.69002 | -58.71704 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fd618057-585e-35e0-b17b-3c70748e2a7f | -7.47241 | -61.37627 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da5aeb0e-d75b-3eb5-bae7-c15c55569a64 | -8.62372 | -54.72328 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8961470-e524-37dd-b1a8-88e7c235367e | -3.09654 | -61.20479 | 2026-08-26 04:51:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bd4ce7b3-fd8d-386c-b27b-c3565ede3f94 | -7.27411 | -45.35591 | 2026-08-26 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e481524d-7567-339f-93d2-b3abf48c58de | -7.56101 | -61.42815 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f605e607-c4a2-35f7-977d-6e20da745000 | -6.94163 | -52.79151 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8e2c744-0f25-34f4-ad0f-22d0e55e96b5 | -8.60848 | -54.73204 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3900354-cd64-3c84-989f-0b59def8b539 | -6.64478 | -58.4991 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| e345e9d7-441c-3e24-b6e0-257085abcbad | -3.53199 | -48.18761 | 2026-08-26 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cf55fe5c-b05e-3375-9185-ff47c44c9ad3 | -6.1532 | -57.9461 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff06460b-74c4-35b4-b75d-3ac3e22112b8 | -8.09849 | -47.56156 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5b3990f-66a8-3b11-b6e5-cf96a4ac211c | -7.26117 | -49.86225 | 2026-08-26 04:51:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 55fbf854-a9f9-3f81-8b96-fc8a49d347b1 | -3.32457 | -54.17897 | 2026-08-26 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a788113f-874e-3ca8-892d-33b1c46b9985 | -9.52563 | -51.67926 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9902538-125b-32bf-b30b-088c64190c60 | -7.27962 | -45.35144 | 2026-08-26 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0c84995e-c5a5-36fb-9081-c16618bdb91a | -10.04318 | -46.04914 | 2026-08-26 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f335c25c-ba83-33bb-8634-22c8f4bc8bef | -7.01713 | -59.23335 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 98983432-286b-3a50-b9b3-0b3ac288538b | -9.91658 | -46.48288 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 426bc360-660c-33c8-ba29-1682dbf5f3c7 | -9.44316 | -51.66677 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 219ee559-0eae-3294-b967-89e9d5f9d69a | -6.72051 | -56.3407 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 167d1e35-a307-3faf-b26d-2f38892fc377 | -6.42233 | -54.94474 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2d36fc4b-e80a-3288-93b3-f10af3130c52 | -5.94227 | -57.72971 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b8b4065-1aaa-3692-8ac1-001d59da18a8 | -6.71682 | -56.3402 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a7cc5ae-3251-3487-b024-10ee998305ad | -3.12661 | -61.18894 | 2026-08-26 04:51:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d028b18a-0010-372e-9f1f-2cb8a08257ab | -7.00763 | -59.23615 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a869cf1-c60b-394c-b218-46a2d8fac22e | -9.27142 | -45.64613 | 2026-08-26 04:51:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2024bb4f-3dcf-3448-9a34-c2ffce0babc3 | -6.17836 | -53.47361 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c972547-dbd8-3f15-98c9-33a07ad760c8 | -6.33849 | -54.74249 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7032320a-890e-31c6-b813-177efd8b1492 | -6.25454 | -53.37833 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6842d9ed-63c2-3ec8-bb5f-9d6489876578 | -8.11292 | -47.46223 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11845bc4-3cfe-3919-95fc-e25beccb8301 | -3.13196 | -61.18979 | 2026-08-26 04:51:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e1fe3ae4-7d7e-3b83-8de1-225ea2de774e | -8.01621 | -51.81569 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a282f84-4938-3062-b716-c77b5eb5af0f | -9.43851 | -51.58269 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6122bbed-b8e3-32f3-b3d1-3c068cc4a0f9 | -9.71769 | -49.33535 | 2026-08-26 04:51:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d96de4f8-6d77-3dca-ba89-06b64a7b7324 | -8.39143 | -47.35912 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 21e585bf-06ec-3870-930b-0487377f1a94 | -5.48417 | -47.42983 | 2026-08-26 04:51:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8045572e-4a3b-3af9-8d3a-f1445a8c5e8c | -7.21199 | -60.61621 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5fa03849-20a0-3242-b309-524db5649f2b | -8.54849 | -54.78203 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8436af1f-2cbe-3a78-90f3-263fded9b56a | -8.1423 | -47.50414 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 398e71b9-9055-35e5-b392-ab30be62a48a | -6.43472 | -54.99294 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 945adf08-e3ee-36bd-9646-2aadfdee3c07 | -7.29234 | -44.08483 | 2026-08-26 04:51:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 09891397-d578-3a63-b040-c7ddb3259fda | -3.21484 | -61.24139 | 2026-08-26 04:51:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3eab50bb-260d-3325-83ca-2b6c549596b7 | -8.57717 | -55.27676 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec204ee0-e0cb-3571-920a-dfae1f667f61 | -6.26056 | -55.41595 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 931c9191-3e38-3194-86c3-7822862e9867 | -6.77457 | -59.44195 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ae8edd39-0a2f-3399-86cb-c7394eed1c74 | -7.3195 | -42.97773 | 2026-08-26 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 8e3d679b-194c-39db-a620-84f3a1084eb4 | -6.51349 | -55.22233 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e46e2bc2-4751-36a4-bf56-543716920c94 | -7.0299 | -59.23846 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cdabc981-e1e0-3c8f-bf2d-7bca26bf699e | -6.89927 | -58.91798 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8320aec4-d1e0-3157-a6e0-ea1bc3acc4e5 | -7.47846 | -61.37137 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f52c1005-7026-34ed-88bf-7ec6d17d3a98 | -7.38934 | -55.15013 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 847d4489-2076-3392-b106-27bf684e19e0 | -2.85145 | -50.46961 | 2026-08-26 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8d2de4f-8675-3c00-bf43-a814b09480ab | -7.37836 | -55.18006 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4739a796-b8ea-3319-a452-1754f6c564c4 | -6.79015 | -59.74441 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a50f0cd-86d7-3e5e-80dd-58c679e9816f | -7.38465 | -55.15714 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8e9cb390-b194-3783-83b3-d9a4927fe737 | -7.0354 | -59.232 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 591cf7a0-9a72-3afe-89a5-bfc8d3a4c775 | -8.59836 | -54.7304 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71959485-9d6a-33f0-8e78-d3d61eb8d5df | -9.03935 | -50.80214 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c9c2a1fa-8eff-3b69-9f77-1004f51a8eb6 | -8.13866 | -47.49962 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| abff1584-5d87-3437-aefa-7ec3c19341a2 | -6.63705 | -58.49375 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f4b2dc6d-c4d2-36a2-a4c6-54a815fa28ed | -2.79288 | -49.5798 | 2026-08-26 04:51:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 17a416d9-04d4-3100-a081-1f671efc40b9 | -8.58829 | -54.83675 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 89146752-5c46-30b7-8cda-5a9c91c5b7a8 | -6.82723 | -58.6528 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1843d803-08a9-3fa8-8281-de91b841b304 | -6.17504 | -53.47308 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5dd5e900-24f4-3aaf-a2d4-e5bcdff5a7fe | -6.14367 | -59.91993 | 2026-08-26 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 260f5ed0-5f06-311e-9cd1-6c28b61b1111 | -10.37208 | -45.06916 | 2026-08-26 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 15932232-9553-3fb2-b7d6-69ab6df54685 | -8.5479 | -54.78569 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31b09841-0637-31d5-9b91-4be0d74958ae | -7.43514 | -59.77722 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 38a58573-a46c-3ad1-be6a-c5c0c2fc58c2 | -9.59937 | -46.00103 | 2026-08-26 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 35185d45-2850-30fc-903e-23f6384e99e0 | -8.57413 | -54.83844 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b9fae2dd-141a-3bed-89b0-24ba638e792e | -6.6386 | -58.51007 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| cd2556c0-aaed-3f2b-9595-a98ea43bf1d6 | -8.62554 | -54.69012 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbc21628-6205-3d82-93f4-c1d23d4ac12f | -6.88953 | -59.02712 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0dbfb27b-6852-3580-8dca-de2a3f774979 | -6.95418 | -56.49132 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4fa51d1c-09a4-3dae-b5aa-ea6d87497a46 | -6.3282 | -54.74083 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 087f60b0-3c9b-3f89-a3d0-803db70bdd2a | -8.61745 | -54.74093 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0b8a0405-b978-38f7-a7c9-67ebfa8dc2be | -8.16934 | -46.18954 | 2026-08-26 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 70c5adac-310d-3801-80fa-81a32917329f | -8.57031 | -55.27562 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f4ef54d3-c2c8-396d-a78e-00c642f40a1d | -8.09586 | -51.67649 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49d0a025-00e1-39c7-94cb-b6b32003191e | -3.10875 | -61.23106 | 2026-08-26 04:51:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 38957a5e-9165-30f4-8435-195a6c73cd56 | -7.29313 | -44.08403 | 2026-08-26 04:51:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e20e42e2-de52-3708-a73d-e918532298bf | -9.72395 | -49.34597 | 2026-08-26 04:51:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a664517e-4da2-3c7a-9664-f6def84e4190 | -6.69367 | -56.16038 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dbe4ef3a-6662-30b2-aa87-2d1d44279ed3 | -9.4341 | -51.68053 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 83dc1158-33fc-3547-b476-b5d67c6f2ac5 | -8.76745 | -49.96888 | 2026-08-26 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8caeb006-14e8-38ae-85ac-266755e2dfaa | -3.13786 | -61.18729 | 2026-08-26 04:51:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b31d632-21fc-35e2-a087-ab819c7d8018 | -5.77002 | -57.55603 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e155edf-bf08-3dfa-8723-d03969fc9753 | -6.02896 | -58.04206 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6defeb82-b39f-3fcb-9bde-e368bd3d8dcd | -7.03245 | -59.22261 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6844307f-5b53-3aee-bf89-c6312e75da81 | -6.84724 | -59.46286 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3222bc0-d161-3056-af4d-30611c4f5354 | -2.59937 | -49.2867 | 2026-08-26 04:51:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e668d269-5d96-3808-bf57-d8ec57f389b2 | -8.60168 | -54.86166 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5af0cc4e-4b6f-39c5-980a-212b1e610dcf | -6.2783 | -53.35705 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67e854f2-da71-3e58-8bf6-184b9746feb9 | -7.52822 | -55.5884 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 577cff04-b6ad-37cc-9931-5a8ed61c118f | -7.0738 | -59.21939 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.3 |


[Clique aqui para ver as próximas entradas](README34.md)
