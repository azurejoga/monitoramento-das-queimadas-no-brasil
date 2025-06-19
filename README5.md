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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a99f409-7a10-3965-9055-96ba0fe4183f | -11.6328 | -58.293201 | 2025-06-19 01:37:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ca8b7d1b-e751-3498-903d-50f8a83e10ab | -18.664101 | -55.760502 | 2025-06-19 01:37:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2ae04049-2a2b-36e8-a9bc-d7e638f666ea | -10.1014 | -52.7449 | 2025-06-19 01:37:00 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6cad4343-f2f9-3aaa-9d91-5b72f4da9136 | -11.6231 | -58.295601 | 2025-06-19 01:37:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a01e07f4-f169-35d4-bdae-b031fffc10df | -14.8367 | -59.8181 | 2025-06-19 01:37:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d9d3676a-386c-3b7f-8552-233de4028214 | -18.66119 | -55.74585 | 2025-06-19 01:37:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.2 |
| 88a3ed1d-c2bc-350f-b6b8-bad2b896ad27 | -18.65401 | -55.7527 | 2025-06-19 01:37:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.7 |
| 27be2221-4279-378b-b065-7f5c35d6927e | -16.32355 | -53.79991 | 2025-06-19 01:37:00 | TERRA_M-M | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 20.5 |
| fc9d3df9-4238-3e63-9843-dc90ef76156f | -18.6641 | -55.76261 | 2025-06-19 01:37:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.2 |
| c311dee5-38ea-3f46-81ac-5b5a6abc151b | -11.9456 | -58.75073 | 2025-06-19 01:39:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 27479bd7-6be7-3fbe-84eb-77af13ac6aa5 | -11.94755 | -58.76372 | 2025-06-19 01:39:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 40.2 |
| f9d9eafb-bf61-3c05-b730-be2a1a6d165a | -11.62603 | -58.29929 | 2025-06-19 01:39:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 5e8fc8ab-e7c0-3842-8810-113af37ca4fe | -10.08842 | -52.7431 | 2025-06-19 01:39:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| c05fa45c-0d45-3e59-8ec0-eccf8c33a351 | -11.95061 | -58.74422 | 2025-06-19 01:39:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 212.8 |
| 2bd082e0-6e07-3e92-961f-642377abcc69 | -10.46213 | -58.68891 | 2025-06-19 01:39:00 | TERRA_M-M | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 3468a70c-4684-3a7d-b5ce-73d2a4889139 | -10.08743 | -60.50112 | 2025-06-19 01:39:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2f0f3486-8b10-3d62-bb92-3cac9d0c433d | -9.45924 | -57.85265 | 2025-06-19 01:39:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| dd58b227-441d-35d0-9a0b-14ce4ab252e6 | -11.62381 | -58.28511 | 2025-06-19 01:39:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 3661f912-322a-33d4-a1d2-23ab05e9f583 | -14.83247 | -59.82257 | 2025-06-19 01:39:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8e29bacb-3445-3991-801a-5f5f757a61cd | -11.52203 | -56.99351 | 2025-06-19 01:39:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 9ae20972-99cb-318a-87bd-12b80da33e63 | -13.5797 | -59.19865 | 2025-06-19 01:39:00 | TERRA_M-M | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 3b03fb20-9c7f-3911-b2b5-1e72b03a3be1 | -12.37339 | -57.40779 | 2025-06-19 01:39:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 98e69d15-c37a-356b-8095-7663dc378e6a | -14.03204 | -55.13224 | 2025-06-19 01:39:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 69eb16bd-42d9-3338-9fa7-87ece1586f9d | -11.96111 | -58.74249 | 2025-06-19 01:39:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 150.1 |
| 5f89066a-495d-3bf8-ad4e-52726bae6861 | -10.08988 | -52.73584 | 2025-06-19 01:39:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 4ae5a2f9-49d6-36df-83a6-701ccc53556e | -11.1342 | -53.95509 | 2025-06-19 01:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 07c68998-07d4-395d-a5d1-41514ec71269 | -11.93703 | -58.76522 | 2025-06-19 01:39:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 7d760b96-8311-3dbb-ba59-1cbd88447e93 | -11.95266 | -58.75728 | 2025-06-19 01:39:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 235.4 |
| 36fb6d9a-e20e-3111-af85-237102f1bed0 | -11.94416 | -58.77162 | 2025-06-19 01:39:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 45434c50-cb7b-3c88-9eee-2a01f90b12ce | -16.29848 | -58.26991 | 2025-06-19 01:39:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 9ba8ae19-1af8-38f3-851f-69d114340c49 | -11.80759 | -57.34943 | 2025-06-19 01:39:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 488601fd-fa16-35be-ba64-2e9b48756f60 | -16.2966 | -58.25765 | 2025-06-19 01:39:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.4 |
| 932a9f54-7804-377c-9408-6c2e1c0fd799 | -12.23473 | -63.60336 | 2025-06-19 01:39:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 7b0e5222-7dd4-371d-98b7-b87b03485a9a | -11.96312 | -58.75536 | 2025-06-19 01:39:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 565922c6-8f31-3ce2-aa99-ef7911ff64ed | -11.95905 | -58.72934 | 2025-06-19 01:39:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 354d5180-03c6-3a23-af8a-662ca8c40832 | -11.13377 | -53.92823 | 2025-06-19 01:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 32.1 |
| dfb2fa91-a948-34b8-8fc3-ca88ca3e9ad7 | -13.58326 | -59.21566 | 2025-06-19 01:39:00 | TERRA_M-M | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| f28dc220-e1d7-3d4b-a086-51e7cde0f36f | -10.30562 | -57.13619 | 2025-06-19 01:39:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| fa9c57ff-083c-3401-87b0-a82dcb7698f2 | -14.02665 | -55.12633 | 2025-06-19 01:39:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 6ec5872d-ae20-3464-91fc-2bd05cabc5cd | -16.30651 | -58.26268 | 2025-06-19 01:39:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.0 |
| 937b49a5-fcae-32aa-9239-3602fd07e71d | -13.58145 | -59.21042 | 2025-06-19 01:39:00 | TERRA_M-M | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 45629b66-adc9-3e18-9abf-5d323751f7cd | -10.08292 | -60.49725 | 2025-06-19 01:39:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b29fd305-8150-386e-9344-9909032de513 | -11.95467 | -58.77006 | 2025-06-19 01:39:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 015491cd-42b2-3559-974d-50cad407fb0f | -11.94216 | -58.7589 | 2025-06-19 01:39:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 15839aee-4b28-3634-ae4e-858447f858df | -12.52556 | -57.20281 | 2025-06-19 01:39:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| ccd89311-c735-338e-9077-50627ac18bfd | -11.96513 | -58.76822 | 2025-06-19 01:39:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| cc8a7dc2-f6c7-30da-b3cf-413d81656ac6 | -16.30457 | -58.25049 | 2025-06-19 01:39:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 34.3 |
| 97f227aa-f2b5-3371-9640-4e8ed950edf3 | -12.52339 | -57.21347 | 2025-06-19 01:39:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 95bc9ff3-a1ff-3904-8fd5-2fe7c36b429c | -12.47233 | -58.47213 | 2025-06-19 01:39:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 2372f166-3fe7-3c61-9bb9-f88e676e6e71 | -13.58144 | -59.20396 | 2025-06-19 01:39:00 | TERRA_M-M | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 3e09d5cd-55f0-3921-b540-21552a3f65a9 | -11.9707 | -58.756 | 2025-06-19 01:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 44d2b288-8a82-38d4-a24a-980f053c3988 | -7.2405 | -43.0899 | 2025-06-19 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 231.7 |
| ca1dee2f-ab9b-3fa5-8342-c2fc16a0ba76 | -4.7872 | -47.5676 | 2025-06-19 01:40:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 8fdb7d50-4c93-3f64-9689-2c5a84d878b3 | -11.9709 | -58.7362 | 2025-06-19 01:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 1ab4601e-b31b-3804-825b-9d4e9d735012 | -7.2408 | -43.0664 | 2025-06-19 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 163.0 |
| 835b881e-9648-32b2-881a-94e9d41de5e6 | -16.305 | -58.2474 | 2025-06-19 01:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.6 |
| 001d15f7-5d23-3fa0-998e-f288fffba279 | -5.1272 | -37.8578 | 2025-06-19 01:40:00 | GOES-19 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 49.9 |
| 2e4880bb-2b66-33a6-a0a7-d187111eeb48 | -11.9518 | -58.7574 | 2025-06-19 01:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 226.6 |
| 933d401c-c98a-388c-8f36-47d881648f56 | -11.952 | -58.7376 | 2025-06-19 01:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 166.2 |
| c85e08eb-0933-3877-9bad-b4c80a71ef70 | -8.0703 | -43.0981 | 2025-06-19 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 60.8 |
| 12177cad-2f41-3e2c-a5df-95330dfac029 | -10.0972 | -52.7376 | 2025-06-19 01:40:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 69e8ac99-4896-30eb-b7ca-da000378a8ff | -11.9707 | -58.756 | 2025-06-19 01:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 138.5 |
| 3bb5eaec-4105-3ce0-a3bf-5ce2a75371d8 | -11.9709 | -58.7362 | 2025-06-19 01:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 104.4 |
| dbcf79e5-b6fa-31a5-a645-2c28a24ea734 | -8.1264 | -43.139 | 2025-06-19 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.7 |
| 8914aab2-ac1c-3a63-8975-c7bc87182a73 | -20.0326 | -45.7572 | 2025-06-19 01:50:00 | GOES-19 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 103.6 |
| eedb4a0a-5b69-3468-a5eb-27e8f813dea5 | -7.2408 | -43.0664 | 2025-06-19 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 134.2 |
| 44b85396-4708-3e2e-a811-f5169fa63b83 | -11.9518 | -58.7574 | 2025-06-19 01:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 191.8 |
| 5141f0c2-04c7-3504-a587-9c5959b85ecd | -7.2405 | -43.0899 | 2025-06-19 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 196.6 |
| acfbc5fa-c472-38eb-be50-ca34f0911aa3 | -20.0128 | -45.7382 | 2025-06-19 01:50:00 | GOES-19 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 3716df89-8d1f-3dbe-9718-47b95c23195d | -4.7686 | -47.5686 | 2025-06-19 01:50:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 62.7 |
| cc0b047f-be14-39bd-8a02-bcd4852f4e03 | -14.4467 | -48.9063 | 2025-06-19 01:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 702c4857-a3b2-351b-9057-46eda1a54a6c | -20.0333 | -45.7331 | 2025-06-19 01:50:00 | GOES-19 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 81.1 |
| d3a57a4c-decb-3594-b4af-9d0634bed63e | -16.3047 | -58.2676 | 2025-06-19 01:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.3 |
| b8dbc595-a292-34c4-9511-41d6b0a40da6 | -20.0121 | -45.7623 | 2025-06-19 01:50:00 | GOES-19 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 95.0 |
| e878f18a-b31c-3960-9bb2-fd1a20b97b31 | -8.0703 | -43.0981 | 2025-06-19 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.7 |
| 92813bc7-f3b4-38e2-bdf6-cefec0dba755 | -11.952 | -58.7376 | 2025-06-19 01:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 461bd3ec-af04-3c1a-ae3c-9818cd115af7 | -8.0703 | -43.0981 | 2025-06-19 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.4 |
| dbdeede1-16ea-39bb-a2ec-c435e1bbe919 | -16.3047 | -58.2676 | 2025-06-19 02:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.6 |
| 64198d91-faec-3b48-95c6-1e76c73f57e8 | -11.952 | -58.7376 | 2025-06-19 02:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 162.6 |
| 38d72ae3-7975-3002-91dc-37a1c3d1c137 | -7.2405 | -43.0899 | 2025-06-19 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 210.9 |
| eccbf005-da5c-3911-a0d5-227281c4de00 | -11.9709 | -58.7362 | 2025-06-19 02:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 5106360a-a399-347e-87db-fbb95193e99e | -11.9518 | -58.7574 | 2025-06-19 02:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 186.0 |
| 0f8c2bee-5f47-3307-a063-a0e6f5ba9614 | -14.4467 | -48.9063 | 2025-06-19 02:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 450f4f6f-5457-36a3-8f41-579d7cce5d59 | -7.2408 | -43.0664 | 2025-06-19 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 112.7 |
| b4a3f115-8d3e-3de4-88b6-ef8dc8639b3e | -11.9707 | -58.756 | 2025-06-19 02:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 20e4f754-2d82-39df-9491-c108f74d12f1 | -16.305 | -58.2474 | 2025-06-19 02:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.9 |
| eccc1100-a733-3d81-8e15-8d7f206b0453 | -7.2405 | -43.0899 | 2025-06-19 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 166.5 |
| 2535be31-d84b-38ca-bd50-a0dbef50d196 | -14.4467 | -48.9063 | 2025-06-19 02:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 74.2 |
| b50312c1-087c-3350-8e5c-c4f9d843b7ae | -11.9518 | -58.7574 | 2025-06-19 02:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 156.9 |
| c5cd8b2a-761d-351e-9148-40349b66981d | -16.305 | -58.2474 | 2025-06-19 02:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.4 |
| 4b36a0de-d730-37fe-a3d5-3c7ff34a1fc3 | -11.952 | -58.7376 | 2025-06-19 02:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 59341058-49df-33ca-9810-fa836b685adf | -11.9707 | -58.756 | 2025-06-19 02:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 2b739451-aa95-3958-874b-0caf51173e34 | -7.2408 | -43.0664 | 2025-06-19 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 110.0 |
| ad162ea8-d3b8-31e3-ae38-e0de0b625860 | -8.1264 | -43.139 | 2025-06-19 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.6 |
| c414338c-3b7a-32b0-8990-532588c7b3ae | -8.0703 | -43.0981 | 2025-06-19 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 81.2 |
| 6f515512-0ac0-34a9-bf37-49f58884329b | -11.9709 | -58.7362 | 2025-06-19 02:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 82dd81b1-da3a-3fda-9179-cb59f20da288 | -7.2405 | -43.0899 | 2025-06-19 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 166.3 |
| 8609e46f-89f2-36c2-a7a1-13a29a8ce771 | -8.0703 | -43.0981 | 2025-06-19 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 92.6 |
| f0295893-78ce-3231-ace5-7135aab90328 | -14.4467 | -48.9063 | 2025-06-19 02:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 42e685f4-45c6-3787-965b-23b14fd2b761 | -11.9709 | -58.7362 | 2025-06-19 02:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |


[Clique aqui para ver as próximas entradas](README6.md)
