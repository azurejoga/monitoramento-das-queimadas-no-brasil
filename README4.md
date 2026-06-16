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
| 6e7f62e8-fa40-3748-8554-9fe6754f90be | -9.36225 | -46.48866 | 2026-06-16 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0491e826-e99b-3d51-ba1b-676f5f4248f0 | -12.06351 | -47.54964 | 2026-06-16 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3947b52-c344-324e-ad3a-e191190d0953 | -11.78359 | -41.19368 | 2026-06-16 03:45:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 23bb8a42-7924-3bd6-965f-449882f6afad | -9.38739 | -40.75528 | 2026-06-16 03:45:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e4999149-40a2-3c7a-9221-17fe6f95ff41 | -8.94657 | -46.96353 | 2026-06-16 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c997f918-03a8-33a3-92cd-ba0f8833cf98 | -13.55559 | -47.86235 | 2026-06-16 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 73729e16-e9e7-3e97-a56c-e6795554fc3f | -8.9481 | -46.96104 | 2026-06-16 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 4f69e7b2-b507-3aeb-aef2-6c9efe3d4ee9 | -9.33005 | -45.48705 | 2026-06-16 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| e760e9a0-c40d-3ce2-82af-8e4bbb8acbd4 | -7.72154 | -44.16161 | 2026-06-16 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a9b53618-96f6-3429-99ac-d42f4291cb04 | -10.88093 | -49.54108 | 2026-06-16 03:45:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4949bb41-4d69-3586-b25f-052b46ba4db8 | -14.85535 | -43.37254 | 2026-06-16 03:45:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 4.0 |
| db7b52ad-f61d-368a-ae83-353f0c10f1a7 | -12.14763 | -48.46737 | 2026-06-16 03:45:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d0fd138-ec80-396d-81b5-b0ea285950d9 | -13.54386 | -47.85943 | 2026-06-16 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3bd5682f-9945-3c3e-8f92-2bcffd9d364e | -14.84646 | -41.3492 | 2026-06-16 03:45:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 52495848-6ed4-3e24-89b0-6384278dca97 | -11.27623 | -44.52927 | 2026-06-16 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37525d08-ac8f-3f9d-b81f-e4710cf7e391 | -11.99028 | -38.96184 | 2026-06-16 03:45:00 | NOAA-21 | SANTA BÁRBARA | BAHIA | Brasil | 2927507 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 205c8233-0b1e-35dd-b0e8-77128a92b8e6 | -14.71661 | -42.94215 | 2026-06-16 03:45:00 | NOAA-21 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c95b5c39-5bbc-3695-bbd8-1c48609325b0 | -8.95685 | -46.94809 | 2026-06-16 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 764e5c3e-d5b5-366e-954a-40968f04e3a3 | -9.01277 | -40.99436 | 2026-06-16 03:45:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0ca0ba9d-3d27-38e2-9212-e6e27b117ca1 | -8.93589 | -46.95917 | 2026-06-16 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2638cb37-1af5-36ce-88dd-cc877493eead | -12.74477 | -46.29106 | 2026-06-16 03:45:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d226207c-0e51-3f02-b9f6-adbedd2526c5 | -11.54688 | -48.26815 | 2026-06-16 03:45:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 55b02b3b-6d18-32d0-b84a-54dd244706e2 | -9.36145 | -46.49282 | 2026-06-16 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c00db97b-04f7-3941-a72c-074f52600522 | -11.11876 | -45.14148 | 2026-06-16 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2467f7a4-233a-3b56-abee-7e123407b0ea | -11.11937 | -45.13829 | 2026-06-16 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9188c64-3222-3ddc-a613-29b09b9f4a09 | -7.72236 | -44.16598 | 2026-06-16 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6ee6f086-76ff-3141-9b84-254c5442221d | -9.32593 | -45.47879 | 2026-06-16 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 810344de-544b-3319-b2f8-82b55c2fca67 | -8.28342 | -48.22237 | 2026-06-16 03:45:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 72c2c3e5-c1b8-395c-987e-0f3201867257 | -8.93499 | -46.96386 | 2026-06-16 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 16a11c2e-c224-3064-8c75-be16fe92af71 | -9.33141 | -45.47981 | 2026-06-16 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a19f86f9-fd45-3d7a-a357-cab8f6350320 | -8.95417 | -46.9621 | 2026-06-16 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 89232e3a-96f3-3a61-8d1b-07d874c2bf71 | -10.55274 | -47.0357 | 2026-06-16 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dda92eec-aa5a-30d3-9abc-afd098b5e4cb | -13.5529 | -47.84533 | 2026-06-16 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b851fa96-380d-3f2f-ac27-a63f5d8eb77b | -12.73859 | -46.29964 | 2026-06-16 03:45:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bcc9082c-4130-34b4-b326-eb8a85fd5fb9 | -13.54788 | -47.8699 | 2026-06-16 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b6fe9759-4f39-3da4-bb5e-c04d3936e788 | -8.942 | -46.96008 | 2026-06-16 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d735950a-93fb-379c-a0b1-e01837c0b29a | -9.21186 | -47.33644 | 2026-06-16 03:45:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ad6e2d9-18a7-35e0-85f1-01c7ab007d10 | -8.94047 | -46.96257 | 2026-06-16 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ea9a2de5-d837-358c-a2d2-94efaac4d27f | -13.53795 | -47.85818 | 2026-06-16 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 433b98f5-77bf-3108-9942-d2c33644bf1a | -12.1329 | -48.26186 | 2026-06-16 03:45:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b49cb24e-a444-340b-bf2b-c4a1044c050a | -11.99186 | -45.146 | 2026-06-16 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4209e93d-d085-392c-8e56-cd831fab42a6 | -10.88064 | -49.54556 | 2026-06-16 03:45:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 392195a5-4ed6-3f78-9eaf-da1b8802a099 | -12.0718 | -47.55342 | 2026-06-16 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 556914ae-ea90-3112-b36c-b906602f2b88 | -8.94744 | -46.95884 | 2026-06-16 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d14b95a0-9579-3a84-9ec5-87f5375a2878 | -9.32019 | -45.47762 | 2026-06-16 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83d3964d-2082-3232-bb4a-cc5b74411ee0 | -13.5623 | -47.85964 | 2026-06-16 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cd0d384d-67ee-3407-9f12-7be80e1eab3e | -9.33825 | -45.47363 | 2026-06-16 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ff360250-7214-3eff-b33f-66081d380297 | -8.95165 | -46.94248 | 2026-06-16 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8667c2e0-ce61-3cac-b57f-de8456e1142d | -9.34306 | -45.47824 | 2026-06-16 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 1d260b60-80fb-3c0a-a8e0-a25066be8a95 | -11.99126 | -45.14912 | 2026-06-16 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5a9563d9-c8dd-3c21-b694-a6f2a0ae5172 | -9.33073 | -45.48343 | 2026-06-16 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 8ddf77cf-6fb9-33f3-8857-6d780c20019c | -8.93927 | -46.97427 | 2026-06-16 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7cf9dd65-f39f-30c7-881a-3110794b4e07 | -12.06948 | -47.55082 | 2026-06-16 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94c250e7-9ecf-36e7-bebb-4b8de9f2dd01 | -9.34373 | -45.47464 | 2026-06-16 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 825d1c89-5f5c-3b8d-bac8-682eeab35a81 | -7.72179 | -44.16912 | 2026-06-16 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5d36d4ba-4340-31b2-a802-d1e0bca04467 | -14.85102 | -43.37172 | 2026-06-16 03:45:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 31902738-0979-368e-b0f1-f8508d8f1f09 | -11.16687 | -45.37183 | 2026-06-16 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ca0bfe0-bc0b-37eb-b8a8-b3a87f905998 | -8.95506 | -46.95746 | 2026-06-16 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 25bfc179-1bdc-370f-a277-2d0483ee32da | -12.8467 | -44.37209 | 2026-06-16 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 9242a009-0532-38a7-8954-fcf035f9116c | -9.33209 | -45.4762 | 2026-06-16 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 62de798e-e1cd-3534-866b-b867e3baefeb | -8.94306 | -46.94856 | 2026-06-16 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 54d2c675-ba03-30fe-9b68-d9cb472242cc | -7.72045 | -44.16789 | 2026-06-16 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b693d6e0-e466-3ed5-9bca-e1813f832977 | -8.94628 | -46.97051 | 2026-06-16 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e31347fb-aaac-3c64-b902-f08ca845aabc | -8.95595 | -46.9528 | 2026-06-16 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 23cb1cdf-bc70-34d3-bfee-7bf06e1de7ce | -10.54764 | -47.03036 | 2026-06-16 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74f9ab03-63a6-326f-a794-9968e1f293a6 | -14.86049 | -43.36897 | 2026-06-16 03:45:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 635e0229-1883-3a02-bf50-11a768ac65d3 | -15.18429 | -41.80709 | 2026-06-16 03:45:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6435ad89-1a0c-3da5-bffc-b6693e077e15 | -9.26748 | -48.57805 | 2026-06-16 03:45:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4a2a45ac-d3f6-3b59-9b4c-00bd227432bc | -8.94719 | -46.96575 | 2026-06-16 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| eb9628ee-6359-3ac2-8b86-0a950bfeed0d | -10.54912 | -47.03697 | 2026-06-16 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a152a580-8d38-39fd-a2bc-05518ef6dab7 | -8.97323 | -47.97844 | 2026-06-16 03:45:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f42108c-4b8e-3a49-b8e5-cb37ac4e0ac5 | -10.54678 | -47.03474 | 2026-06-16 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7b9213a8-ec76-33fd-8153-e3e5de48f147 | -9.2171 | -47.3425 | 2026-06-16 03:45:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6ff9048-a6c3-3c74-9c91-0d64ac58f786 | -13.21161 | -45.48842 | 2026-06-16 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70bf8738-4497-3df2-96a8-a0d570197be7 | -14.55281 | -42.08635 | 2026-06-16 03:45:00 | NOAA-21 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 647dec30-f06b-327a-9d1b-91d1d7563d77 | -13.8134 | -43.65079 | 2026-06-16 03:45:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49976e3f-3fe7-3d12-97c1-94ec5b1d3bf2 | -12.02692 | -47.80656 | 2026-06-16 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| adfaaae3-0002-3c1a-afda-7da0c9eef0fc | -12.06582 | -47.55233 | 2026-06-16 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c14a048e-bafb-3b90-be96-cf98d268aa37 | -8.94018 | -46.96955 | 2026-06-16 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 83b16a66-5d63-3dc1-b9ac-5b2589a03834 | -11.99066 | -45.15224 | 2026-06-16 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cf238901-4935-3864-bc8f-19cf8ee7db71 | -10.54848 | -47.02606 | 2026-06-16 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fbac7367-78ad-367e-87b2-25ec26254582 | -10.50874 | -44.85992 | 2026-06-16 03:45:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ac2e3f7-0a99-3cf0-993d-4c32af11bfbf | -15.06938 | -41.97424 | 2026-06-16 03:45:00 | NOAA-21 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 358a5670-98b1-368a-82be-4690b591c770 | -13.54882 | -47.86531 | 2026-06-16 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 829529fe-3ccc-38ba-b632-56b8033078e4 | -9.3681 | -46.48975 | 2026-06-16 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9234b903-575d-3681-b226-2f585b3d4dc6 | -13.55219 | -47.84882 | 2026-06-16 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6bf1b546-dc13-3112-bfc7-e70d1c062e62 | -7.721 | -44.16474 | 2026-06-16 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 97d9f8c5-cb72-3f92-a289-4aec8cbbd035 | -8.28211 | -48.21728 | 2026-06-16 03:45:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2d5d7707-cc2f-35b2-b697-019a0f861bc0 | -9.21802 | -47.33768 | 2026-06-16 03:45:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 070ddca4-09b0-31bb-83ab-a42e81c0c6d1 | -8.93871 | -46.97208 | 2026-06-16 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 711b13aa-ec93-3022-bac5-9744aa8c4b59 | -12.13132 | -48.26057 | 2026-06-16 03:45:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ea1f725c-ad8f-31a3-8283-3cd2f7a4c10f | -14.20494 | -42.56949 | 2026-06-16 03:45:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 94a46541-d6bf-34ff-ad0b-0d423642ea57 | -13.56139 | -47.86409 | 2026-06-16 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1e544fe2-8b41-3df1-961c-17488419ff60 | -8.19265 | -46.76252 | 2026-06-16 03:45:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e7a81557-f231-3ea0-a4ed-2e886e712dd5 | -11.27568 | -44.5322 | 2026-06-16 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39efbbac-0d10-31cf-9079-3bd6758c1cb3 | -12.14869 | -48.46215 | 2026-06-16 03:45:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a08c1b68-5faf-3168-a40c-7794e3ccc385 | -14.85616 | -43.36818 | 2026-06-16 03:45:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 458dd29e-47af-32d1-bd8f-1ea4b92f1f60 | -8.93959 | -46.96733 | 2026-06-16 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b4a5f06f-37cb-38d6-bda7-3e206577372d | -8.94898 | -46.9564 | 2026-06-16 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 4b78d4f4-b0c1-3417-93ec-8b52b3a8402f | -6.83953 | -47.90789 | 2026-06-16 03:45:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README5.md)
