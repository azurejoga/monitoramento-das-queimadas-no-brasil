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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d38eb39-7abb-3091-818f-67415bb20c0b | -8.9427 | -45.68 | 2026-06-24 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| ff47e2ec-7968-3e18-8831-c4e2d5d38f3b | -11.2407 | -43.3464 | 2026-06-24 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 155.7 |
| 7372c50a-e725-38d9-a548-ef12db4321d9 | -11.2216 | -43.3493 | 2026-06-24 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 138.9 |
| ad0e793b-880f-351e-97e2-2aef89703e4b | -11.318 | -43.3109 | 2026-06-24 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 5eb1af91-8b96-3431-bb0e-a1e7989ba68f | -12.8354 | -44.3657 | 2026-06-24 14:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 74815d2a-9885-30c8-b7d9-133c3540899b | -12.8552 | -44.3389 | 2026-06-24 14:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 131.8 |
| bbe6eb71-3af9-3a7d-bbb9-9d21da52ab94 | -9.7439 | -47.8908 | 2026-06-24 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 4076642e-a9c1-335d-9cb7-67d4b604a0f2 | -11.4694 | -46.7271 | 2026-06-24 14:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 117.9 |
| f3bd404a-20b9-371a-b30e-3f08462eba2e | -12.8552 | -44.3389 | 2026-06-24 14:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 4df04ac5-9e0c-30ee-bd55-c9830991ec8b | -11.2216 | -43.3493 | 2026-06-24 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 543.4 |
| 3f64e26a-4c81-3866-9638-374a0279e410 | -11.591 | -47.4496 | 2026-06-24 14:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| af000614-8992-3c13-a1f2-ae0d9cb6b886 | -11.2211 | -43.373 | 2026-06-24 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 170.7 |
| 4b48b115-1608-34ba-a7be-af928582d437 | -9.7442 | -47.8688 | 2026-06-24 14:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| a6332807-a0ba-3d25-80d9-11d2d3a62de1 | -11.2403 | -43.3701 | 2026-06-24 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 111.4 |
| f40088e8-3ab1-3e4a-8dda-0fc4c37fd5f6 | -11.2407 | -43.3464 | 2026-06-24 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 234.7 |
| 53bb83ea-0b97-3c2f-8ed6-fb2454317ee0 | -8.9427 | -45.68 | 2026-06-24 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.9 |
| e01195f0-1f56-34ab-ad9d-82c9a4c5a1fd | -6.5924 | -43.8957 | 2026-06-24 14:50:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| a4287c05-c197-3d2f-a812-0a88b2f5a96e | -12.8354 | -44.3657 | 2026-06-24 14:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 74b826ef-1bcc-313e-8fec-a5514760625c | -12.8552 | -44.3389 | 2026-06-24 15:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 147.2 |
| ddcc7787-f891-38a3-8ea7-7d6d6ea3209f | -9.7439 | -47.8908 | 2026-06-24 15:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 498029d6-d528-3782-899b-f01b453c1f47 | -8.9427 | -45.68 | 2026-06-24 15:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 03948473-3bcd-34f6-b7e6-e127c4f994de | -9.7442 | -47.8688 | 2026-06-24 15:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 4466891b-2f86-3328-b809-a95515bc4aa5 | -6.5924 | -43.8957 | 2026-06-24 15:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 88de7987-2bd9-3a9d-b6b5-048587148de3 | -12.8354 | -44.3657 | 2026-06-24 15:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 1b1f3002-ad71-30dd-a3f4-9849ffcad373 | -11.2988 | -43.3139 | 2026-06-24 15:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 3eef2308-9f24-38ac-bc46-f2e3eabeb4b0 | -11.2211 | -43.373 | 2026-06-24 15:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 96.2 |
| e49e761d-ad2d-327c-9620-1f83c9433172 | -6.5924 | -43.8957 | 2026-06-24 15:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 50ba5463-6921-369c-ac47-af3cc9b140af | -15.7629 | -43.239 | 2026-06-24 15:10:00 | GOES-19 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 82.4 |
| e2a8616a-32bd-308e-97fa-08eaafaf85fc | -11.2216 | -43.3493 | 2026-06-24 15:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 368.0 |
| df2af6c1-71e5-358f-83ff-5cbd494a7ee5 | -12.8354 | -44.3657 | 2026-06-24 15:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 173.5 |
| c581e320-96a8-3900-a6ac-9dfc93577618 | -10.3566 | -50.0815 | 2026-06-24 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 8802c00c-177d-3649-9789-bb0bca45797a | -11.3175 | -43.3347 | 2026-06-24 15:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 136.1 |
| d3e96f37-a287-3e65-b2d5-0d256c6819bd | -11.318 | -43.3109 | 2026-06-24 15:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 171.5 |
| af3557f2-cb22-378a-bc62-bc05534820cc | -8.9427 | -45.68 | 2026-06-24 15:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 10e30874-796b-34f7-8abd-330f589c5c31 | -15.7635 | -43.2146 | 2026-06-24 15:10:00 | GOES-19 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 141.0 |
| 4972c514-730a-35f7-88b0-329b2dfb9f01 | -11.2407 | -43.3464 | 2026-06-24 15:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 181.6 |
| 651bb1d0-c515-3ef6-8c39-15f1ff03e5f0 | -9.7442 | -47.8688 | 2026-06-24 15:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| d4337fe4-1f07-30b7-a4f5-c4f9229311c5 | -11.2211 | -43.373 | 2026-06-24 15:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 211.3 |
| 8328c3ca-db05-3e90-bc68-598bd6216656 | -10.6606 | -49.9637 | 2026-06-24 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 137.0 |
| d473efad-b92f-3e24-9598-d552468fb563 | -11.2988 | -43.3139 | 2026-06-24 15:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 5ff6e990-5002-3014-8bf8-15e34f204ece | -8.9427 | -45.68 | 2026-06-24 15:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 3d81036a-73e5-3ead-a9cc-7b3d5c50eea9 | -6.5924 | -43.8957 | 2026-06-24 15:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 4d049a20-9e2e-3ede-95bf-e3bb0b17a248 | -12.8354 | -44.3657 | 2026-06-24 15:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 4c04ac10-0e8b-3125-884a-b5fd2fd35582 | -10.3566 | -50.0815 | 2026-06-24 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| f730ad0e-e246-3453-a3e3-d41acc8382a4 | -11.2407 | -43.3464 | 2026-06-24 15:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 248.0 |
| d403f89d-3f1b-3c21-86c7-b1eef34d8fc4 | -8.7844 | -44.8085 | 2026-06-24 15:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 36f747f2-920e-3376-88e6-8d98fc4bb456 | -6.5922 | -43.9189 | 2026-06-24 15:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 23f8bbb4-ee8b-3ca1-bf18-6407b9686a9b | -12.8354 | -44.3657 | 2026-06-24 15:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 145.5 |
| 5abcf18a-1365-3f77-aa0b-96893ace3831 | -11.2407 | -43.3464 | 2026-06-24 15:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 325.1 |
| 21cf3179-adb6-3c15-9580-e65d4fded0bd | -9.9016 | -53.4148 | 2026-06-24 15:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| c35ce8b4-827c-3e6c-a9fd-7f5873e91681 | -11.2988 | -43.3139 | 2026-06-24 15:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 29db7b41-209f-3af8-84cd-d6e704ad6e49 | -6.1246 | -45.7792 | 2026-06-24 15:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| dd50ba9a-3e8e-3fa3-916a-d335f3604981 | -6.5922 | -43.9189 | 2026-06-24 15:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| b9a08274-a65e-3367-8dcb-28325e5d7cf3 | -6.8767 | -43.6618 | 2026-06-24 15:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| fe50cc29-5042-3ca8-a055-a921ef0a2f09 | -10.6796 | -49.9617 | 2026-06-24 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 596553a3-2a35-30d6-b551-da5a0ec92afc | -11.2216 | -43.3493 | 2026-06-24 15:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 307.1 |
| 97d41e89-bc56-3a85-817a-4125296a3574 | -10.3566 | -50.0815 | 2026-06-24 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| c779976b-24e4-3def-b0e5-af3239d71280 | -6.5924 | -43.8957 | 2026-06-24 15:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 2646d567-4874-3163-8a53-41afef6643f0 | -12.8354 | -44.3657 | 2026-06-24 15:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 17edda05-d6e6-383e-86d8-4ff56abf8dbe | -6.5922 | -43.9189 | 2026-06-24 15:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 1255055e-d9ae-3d39-888c-2e421777daa5 | -10.6796 | -49.9617 | 2026-06-24 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 232.6 |
| c7fce50b-a947-3598-8e1f-92cac5038746 | -6.5924 | -43.8957 | 2026-06-24 15:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 175395e1-6258-3870-ac10-039d94f3d009 | -10.6606 | -49.9637 | 2026-06-24 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 144.4 |
| cdf8e183-1bd5-31ff-8763-4fb869860052 | -6.8767 | -43.6618 | 2026-06-24 15:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 72.2 |
| e87ba9b9-3728-32ed-9ce2-ebf2a2c11cd4 | -11.2407 | -43.3464 | 2026-06-24 15:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 182.1 |


