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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4489374c-0aa3-376c-ad73-dc9316510d11 | -8.03327 | -47.40892 | 2025-10-29 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e7cae41c-255a-314d-8356-69cf2876da9b | -5.61318 | -45.19162 | 2025-10-29 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3426f1c6-5494-3e90-aff6-615a8d0d64c8 | -9.54144 | -46.92333 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6d77846b-4fe0-35e7-9565-c945fd609a25 | -8.48959 | -47.49535 | 2025-10-29 04:23:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c6fce19-1576-37eb-a6aa-7856713c2fd4 | -7.22559 | -46.72135 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ccc6493-1d36-3c3a-94b9-4958d3e4555e | -10.52111 | -45.04866 | 2025-10-29 04:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4b4547dc-0f67-38f8-8801-4a2235352241 | -6.1338 | -41.70697 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| dedf7723-e1a6-3983-8011-c56813a0535d | -8.09073 | -45.95084 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ddbd8ce9-d47c-3cc5-90ce-24ce9b9cd832 | -7.07266 | -44.95298 | 2025-10-29 04:23:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9f0ca54f-5115-3369-ad95-0e0755dc5fe0 | -7.80532 | -46.46159 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f9509567-26ca-3343-a875-18219cf75d48 | -10.37247 | -47.14116 | 2025-10-29 04:23:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f63c8a46-774d-32f8-9866-4f24252c1f78 | -7.30537 | -46.31471 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9f360637-6dae-370a-817b-43e215ce6d5e | -7.78443 | -46.46198 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 328974ac-61e3-359d-b113-4179406574b7 | -9.85516 | -44.87848 | 2025-10-29 04:23:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f07edde7-7f95-36a5-919a-984629707003 | -10.76682 | -47.89353 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 051cef2b-4f91-348f-9460-f5cbbc987d91 | -11.17826 | -43.43255 | 2025-10-29 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 145fa270-8a67-38b3-9b35-08da7d46250b | -6.00591 | -43.31618 | 2025-10-29 04:23:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a9e2f2c4-0cc1-3627-b8c2-3baebffebb74 | -6.21172 | -41.82915 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f285895b-47bf-3cbe-b55b-579d16b54ce9 | -5.17625 | -44.92259 | 2025-10-29 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a72ee322-996e-39c6-99fa-df25bbed3196 | -7.352 | -47.64775 | 2025-10-29 04:23:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6af17119-8446-3453-a4c3-11482c3ac91a | -6.10603 | -41.74425 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 589915c9-b240-3bc4-bdff-67ceb67c565c | -9.8965 | -44.89213 | 2025-10-29 04:23:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d174dea4-cf7a-33ba-9e81-4ff9a2fd0faa | -7.08096 | -44.94361 | 2025-10-29 04:23:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 03d514d4-4c5f-3147-ade6-570a5614b2f0 | -9.89131 | -47.45138 | 2025-10-29 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6eea77f5-f6f6-3f60-a3d2-455323dcfd35 | -10.98911 | -47.85863 | 2025-10-29 04:23:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c4c4ece-1c5a-3f1b-8466-319e16d7472e | -7.15883 | -47.26203 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| afe18bfd-6007-3ad6-ab6c-824a890fd032 | -11.28754 | -45.01014 | 2025-10-29 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4c7a84f8-b3a3-3447-930f-153e1be88c07 | -6.64702 | -43.61291 | 2025-10-29 04:23:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b3317a6-200f-34ad-a331-7780a75e2adc | -7.80383 | -46.42794 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 249d52d7-d7d3-3f64-9b43-b04f7e528629 | -10.65114 | -47.76427 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86117672-cb41-39aa-a455-cb288f713951 | -6.47947 | -42.2422 | 2025-10-29 04:23:00 | NPP-375D | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 57109214-006d-3e90-8897-e091c32517cb | -8.72783 | -49.76901 | 2025-10-29 04:23:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aad89010-07e9-3426-9270-5b5c2bda080c | -6.11145 | -41.73283 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d339c368-bd84-3e2f-ae74-27acd9e163e5 | -10.44256 | -44.70169 | 2025-10-29 04:23:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc2120d4-1696-3ea2-a755-7475020354e6 | -8.54818 | -45.69535 | 2025-10-29 04:23:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0448d86e-ee0d-3993-b9e8-8b5accd2c6f9 | -7.61418 | -43.5845 | 2025-10-29 04:23:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a78e31f3-2270-3544-8ece-ef77378a8d10 | -6.14184 | -41.6858 | 2025-10-29 04:23:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d4ce84b0-7cdc-3c2a-872b-821a3ca46ced | -6.46891 | -42.2407 | 2025-10-29 04:23:00 | NPP-375D | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 47f6e771-a02f-3bdf-a0c9-14ff9c691d1a | -7.16074 | -47.25033 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 379782a2-c928-3ccc-8204-dc76ef44ffbc | -8.33567 | -46.16021 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ac63ff5-95fe-3bff-83bf-aca52a6a27cf | -10.22271 | -45.93705 | 2025-10-29 04:23:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 44cae204-6483-3968-a1de-0cbc6f6ba315 | -9.05408 | -45.04953 | 2025-10-29 04:23:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80e1d41a-5369-3c20-8054-33393d733e5b | -6.13539 | -41.85061 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3635321c-5738-3f12-9450-baff5c7b9ccd | -6.15218 | -41.81202 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e28142f8-c692-3da5-b839-25b2e2b9d2be | -8.51899 | -44.09601 | 2025-10-29 04:23:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3c039ce4-eede-3fe9-950e-43194ae22f23 | -6.95973 | -45.02403 | 2025-10-29 04:23:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c522c38f-1ad3-3f3f-85e1-7b6db9da38fc | -5.68088 | -47.82974 | 2025-10-29 04:23:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8157f39d-af2b-3bec-9774-7724ed97981d | -7.74413 | -44.72477 | 2025-10-29 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 532e06c1-643b-3e4c-9b19-823a350d2ea2 | -5.60027 | -45.35819 | 2025-10-29 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1eddd8c-6afa-3f6d-afe4-8de0dd3f4288 | -5.54229 | -48.06485 | 2025-10-29 04:23:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 73b65e2b-2dfb-384b-a691-55b936fd59cd | -5.74655 | -41.90173 | 2025-10-29 04:23:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 22630d53-06cc-301d-b978-0643db9fd86b | -10.64807 | -47.99974 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 083de8d9-1f3d-3bff-9eac-23a32911769b | -7.96674 | -46.73817 | 2025-10-29 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 095ed7e9-fe8b-3f03-beea-2da8de9027c1 | -10.57338 | -49.75336 | 2025-10-29 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d8c5eb83-f826-3b4f-b4bb-9132d4290e7c | -10.52631 | -47.7364 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1a1e43b-7ca8-334b-a56e-ed6176403895 | -7.80591 | -46.45795 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2ea8bc2d-b475-37b8-bab6-27bb9e5f57c2 | -7.69304 | -46.28533 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f74450ab-4b22-3e43-ba06-7bc40bfc9279 | -6.65038 | -43.61343 | 2025-10-29 04:23:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0e6d8e3a-326c-31cf-b314-d330f6ee01d8 | -5.71204 | -49.30327 | 2025-10-29 04:23:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59924974-e64f-3490-8879-b8589c40a17b | -10.64994 | -47.90133 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0bf87989-baf3-30e8-92f9-8bbac74cf92b | -6.9898 | -46.23421 | 2025-10-29 04:23:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6e9594e-b77b-37fe-8dc6-3b2256ad7049 | -6.25049 | -41.80462 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7ce0ac35-de17-31f4-8ea2-2628a80a7dd1 | -6.09894 | -42.44267 | 2025-10-29 04:23:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| f8f46238-9f0f-3387-8e2a-524113c2c0c7 | -9.58972 | -46.42474 | 2025-10-29 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c46046f1-d07d-310f-89f6-17572d4c356a | -9.92107 | -47.12073 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 785f339c-1d4e-31e8-b0a6-6273bba94fc0 | -9.57213 | -44.71392 | 2025-10-29 04:23:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db6c2f17-f785-325d-91a7-54996b76534d | -6.27233 | -42.09082 | 2025-10-29 04:23:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0fa20fc4-0d98-3927-8738-465e1483dcb6 | -7.95344 | -45.4541 | 2025-10-29 04:23:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a3400cdd-76a5-3546-a2a4-5565567b7738 | -10.63888 | -47.90364 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5420f072-31e0-3923-842f-0389fa8bf846 | -5.42721 | -46.34715 | 2025-10-29 04:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34062062-574f-3c10-a207-7a39af6c0c9b | -8.54631 | -45.69187 | 2025-10-29 04:23:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48d1eab3-8127-3cd8-9a3c-654b399922a8 | -7.31674 | -47.82001 | 2025-10-29 04:23:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1df2bc56-f07a-3fd6-91f5-cd89401ef3fb | -10.52097 | -47.74727 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0c12ac0e-9288-3f44-bd82-9960dad1fba4 | -7.49053 | -47.04111 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 289c9c1c-ce7c-3f9d-861f-c97af02f6eb3 | -6.10767 | -42.43227 | 2025-10-29 04:23:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5658bb13-702f-3bf9-8b8a-8e2ada6a096b | -7.07873 | -44.93614 | 2025-10-29 04:23:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c785927e-71ce-3517-80c8-824b74cd3338 | -10.369 | -47.13719 | 2025-10-29 04:23:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58b4bf97-244c-3d7c-84e7-1bdd0bf7aa80 | -9.90042 | -44.91081 | 2025-10-29 04:23:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4eda352e-bd8a-360f-ad24-20761be2cd2c | -10.54469 | -44.59694 | 2025-10-29 04:23:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ccccf68-aece-3367-a7df-cef85e8b525b | -7.91165 | -45.67318 | 2025-10-29 04:23:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 313c9d47-c7b9-3b28-85e0-156c0846936f | -10.50646 | -45.38208 | 2025-10-29 04:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b0e3cbb-01da-370a-a68e-1868acd67b2a | -9.92447 | -47.1213 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 10bab497-fda8-3bf6-b4f4-4db426c9e862 | -9.92754 | -47.68324 | 2025-10-29 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ec2ca3d4-4c9e-3884-9385-dc70acd8b92f | -9.56879 | -44.71338 | 2025-10-29 04:23:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ed5a24e-cd5c-394f-babb-c0d182317904 | -10.33157 | -47.21779 | 2025-10-29 04:23:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5883eef-b668-37b3-9ce0-0ef53a535458 | -7.3409 | -42.47351 | 2025-10-29 04:23:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 35e7b8ff-ea0e-3cfc-ae62-c780f1a7167c | -9.54543 | -46.92022 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a705f04-e1cc-3b7d-98f4-f2e1374bb29a | -7.80252 | -46.45741 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 875d8874-56fb-3763-b7c3-0c2e1f7e3b2b | -8.54353 | -45.68781 | 2025-10-29 04:23:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65ec6538-7016-3d54-96db-796a8eb2925e | -7.26975 | -46.89631 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8540bb5f-b3dc-3ce1-b8ed-58af835978da | -9.09035 | -47.81434 | 2025-10-29 04:23:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0612d2f-6656-3e69-b7cf-7ed675c28142 | -7.4946 | -47.03788 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 046aff98-7158-3527-8630-e41b10897234 | -10.83581 | -44.95693 | 2025-10-29 04:23:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6698de8-5199-3e06-a4e0-bb833b0fd601 | -9.39174 | -54.60466 | 2025-10-29 04:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d309ed7b-13aa-339c-a8d0-43c75cf1dabb | -5.41362 | -45.21397 | 2025-10-29 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 27cbb16b-0967-31c7-a36e-f3414c5777ca | -7.44301 | -45.11523 | 2025-10-29 04:23:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 404f59cd-57c8-3dcf-b578-e5c43be42941 | -6.92166 | -46.0288 | 2025-10-29 04:23:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf3f19f7-ca30-3897-8f1c-76aaaf8cc935 | -8.24368 | -46.90691 | 2025-10-29 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45618888-7404-396c-b098-cd7d022b7fc4 | -8.69354 | -47.13086 | 2025-10-29 04:23:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bfe8d79d-e593-3e8b-a9c8-32b8612846e1 | -8.38366 | -47.74362 | 2025-10-29 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README41.md)
