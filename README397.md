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

## Dados Diários - Página 397

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb357ed3-19b9-3c28-ae5b-41cd6a33b699 | -6.8764 | -43.685 | 2026-10-08 18:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 0eb7872c-b675-3e54-9b4f-d90915436230 | -5.5146 | -42.8399 | 2026-10-08 18:40:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 96.3 |
| 023cc62c-b5bb-345a-963d-ee02fb79dfff | -11.6177 | -43.6906 | 2026-10-08 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 218.7 |
| 2539f1aa-d5bc-3819-8279-bcac236b6f20 | -3.2957 | -49.1202 | 2026-10-08 18:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 9d57fbc0-42f8-31f9-8aa9-60ffddba3d56 | -4.3726 | -55.6449 | 2026-10-08 18:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| a1d17733-8e7c-345f-beda-4fb7b8589c0c | -1.5489 | -54.5556 | 2026-10-08 18:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 215959c6-dc6e-3a56-9414-0299c40b18d9 | -2.2803 | -48.7654 | 2026-10-08 18:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 7574a923-2eee-3a7e-895a-1cc8740bcba2 | -14.4522 | -40.6611 | 2026-10-08 18:40:00 | GOES-19 | BOM JESUS DA SERRA | BAHIA | Brasil | 2903953 | 29 | 33 | nan | nan | nan | Caatinga | 137.2 |
| 0f2df608-4d1c-390f-adf2-f4ac1ed8617f | -6.4905 | -55.9563 | 2026-10-08 18:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 217.0 |
| 6c8038ca-1f83-3c08-8040-e106bfc985cb | -3.7166 | -54.2297 | 2026-10-08 18:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 65bf0ef5-5a9d-36cb-9231-d823501bfb88 | -1.8233 | -54.9307 | 2026-10-08 18:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 99c656c3-9c3f-3164-96d3-ad1661e06599 | -1.8232 | -54.9904 | 2026-10-08 18:40:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| e89ec895-9744-31f4-abdb-c9fc0bad9fd1 | -9.9011 | -44.8378 | 2026-10-08 18:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 313.7 |
| 3aa4cce3-37e3-3629-ba0f-7e965dd9878f | -6.0076 | -53.4919 | 2026-10-08 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 116.7 |
| 0b55687a-2adb-31db-aa79-f2f42cf5fb77 | -2.8434 | -57.4696 | 2026-10-08 18:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 115.1 |
| 3d3babb8-50d6-3791-8f48-17e1f7936774 | -1.6213 | -55.1123 | 2026-10-08 18:40:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 0b8fb97b-953e-31d5-b1c2-0486329d5cfa | -11.7335 | -43.649 | 2026-10-08 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 307d9d4f-fab1-3cb1-811e-4a04b1b1f9a6 | -5.9955 | -55.3631 | 2026-10-08 18:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| ae9bef05-42db-39d8-8835-c98a5b4b5ecb | -5.9936 | -55.6815 | 2026-10-08 18:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 97e01fae-169f-33be-98e7-8317f57b786f | -9.4819 | -66.7836 | 2026-10-08 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 113.9 |
| bee70901-15d7-3115-b2d9-ad1e23c3aad2 | -2.9265 | -54.1305 | 2026-10-08 18:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 76cd9fb4-ab63-36aa-9a87-d9f589ce2bde | -3.1787 | -50.5807 | 2026-10-08 18:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 193.6 |
| 75f8c109-a475-3801-a267-731737b1a636 | -1.3264 | -56.4176 | 2026-10-08 18:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| e0b05e55-213e-3514-b757-e90d737b0c47 | -6.6224 | -53.0105 | 2026-10-08 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 8d5c55c1-4fcf-3795-b036-8593dc35da9a | -5.2661 | -45.726 | 2026-10-08 18:40:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| c76361b8-7b76-3677-9b13-b1da61cc9019 | -7.4975 | -55.0055 | 2026-10-08 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 109.0 |
| f1e7076b-263d-3a72-94c5-dfb87d06b3c3 | -11.0953 | -44.0037 | 2026-10-08 18:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 157.1 |
| d58cee70-5701-328d-9106-2b14d971f8cb | -6.2157 | -52.8695 | 2026-10-08 18:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 169.3 |
| d7ff81fb-e918-32bf-9cc8-02227309a60d | -2.8347 | -54.1125 | 2026-10-08 18:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 7a55d8aa-41d7-3c90-8916-73900200c424 | -2.853 | -54.1322 | 2026-10-08 18:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 0b3413d8-dd77-3487-8155-35002ca9d92d | -6.4753 | -55.46 | 2026-10-08 18:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 649b0262-d08c-3357-98f5-72c4923cbdb4 | -2.5903 | -56.1642 | 2026-10-08 18:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| cd38c512-6e49-330c-b861-ea0e69af502d | -5.6934 | -53.4667 | 2026-10-08 18:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 557.2 |
| 16f44c11-13d4-3e01-9bf0-ceb4fe73acc7 | -5.3763 | -45.943 | 2026-10-08 18:50:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 8d766138-5454-3b98-be09-8d81743eb010 | -11.7738 | -43.5482 | 2026-10-08 18:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 5338f261-7d2d-334d-9a48-a6698cf9f097 | -5.4806 | -44.6029 | 2026-10-08 18:50:00 | GOES-19 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| abba215d-e489-3be7-b39d-c9ed614d5a72 | -1.1094 | -54.1601 | 2026-10-08 18:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 0edae88b-a62c-3096-9aae-3131b43d18dd | -6.0386 | -51.7261 | 2026-10-08 18:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| eb091b32-8990-3c30-a2ef-2f11e50d1c04 | -3.2957 | -49.1202 | 2026-10-08 18:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 9d5aec82-f51f-3c16-8912-f6fc6002eae2 | -8.5313 | -46.911 | 2026-10-08 18:50:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 82f544c9-a01d-3684-b85e-3d10b7c4d7d4 | -2.2297 | -53.7026 | 2026-10-08 18:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 69adb1f3-418e-37ee-a2ef-f0389a05b21d | -6.1617 | -52.6471 | 2026-10-08 18:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 03e08fc1-8619-3bba-a7f4-dbf3bb639446 | -5.9772 | -55.344 | 2026-10-08 18:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 2777d732-21b2-3088-8955-93f507688a55 | -9.3395 | -65.4451 | 2026-10-08 18:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 123.8 |
| f9a406c1-3f11-32de-8176-9f0a40f00fd2 | -15.1248 | -43.6369 | 2026-10-08 18:50:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 148.7 |
| 210cf5e6-06fc-36af-9bd7-fdeaf45cae32 | -3.3139 | -59.3898 | 2026-10-08 18:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 137.1 |
| dd1d4350-b511-32d7-8617-bdf36867abbb | -3.1697 | -58.6244 | 2026-10-08 18:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 106.0 |
| bb3b0fa2-302e-3c3a-8c32-905a61944be9 | -9.9398 | -43.5542 | 2026-10-08 18:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 99.5 |
| c1cb50e2-3ccd-3e27-a1ca-c701f7f0bf23 | -4.6641 | -56.2281 | 2026-10-08 18:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 32363f57-b7fe-37f6-92e3-acbf4f33f369 | -1.3264 | -56.398 | 2026-10-08 18:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| e1ff7bfd-743a-3cdc-a104-42c7f8f1c26c | -11.1988 | -49.4297 | 2026-10-08 18:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| cb15a030-d6fe-3507-83e7-cd1b6a48728a | -3.2634 | -57.8689 | 2026-10-08 18:50:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 199576b8-6e66-3008-80bd-32ea655371d5 | -11.2083 | -45.217 | 2026-10-08 18:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 18caf4f9-a422-31e0-9299-7215c6883556 | -5.177 | -45.1912 | 2026-10-08 18:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| d4234626-52b8-3541-a3e9-7072eb862e3a | -3.0799 | -58.0083 | 2026-10-08 18:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 41ff776b-f280-38e0-99ce-05c3fcd90a15 | -6.4567 | -55.4809 | 2026-10-08 18:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 126.7 |
| 5bec491e-e352-3afb-8963-ad6fa32844bf | -7.184 | -46.5225 | 2026-10-08 18:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 36e599b4-9aee-3f45-9097-1f8327696cc1 | -5.4956 | -42.8648 | 2026-10-08 18:50:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 129.7 |
| 26d7ca44-d929-3f2d-a6a5-2ec7bef13fa1 | -4.1023 | -44.1379 | 2026-10-08 18:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 43fb173f-7071-3f24-9a19-9a78182f86eb | -2.9455 | -53.929 | 2026-10-08 18:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 16077c6f-0a49-3eb0-9f18-bd19def9fb22 | -5.2274 | -48.4113 | 2026-10-08 18:50:00 | GOES-19 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 5c165bc4-9259-30cb-a6ce-8291828bfbc4 | -5.3718 | -44.1981 | 2026-10-08 18:50:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 2b6a78af-5b5e-38b8-bc0d-c0d304dddd0e | -6.4568 | -55.4609 | 2026-10-08 18:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 08dcd994-7df9-372a-aa8a-fb3cbeea61e3 | -0.5993 | -49.4293 | 2026-10-08 18:50:00 | GOES-19 | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| f88bacf0-4a45-3e10-9057-d930e1385c31 | -5.8599 | -53.4586 | 2026-10-08 18:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 114.1 |
| aed0c08d-1eea-393c-8e42-91036c537d6b | -2.77 | -57.5293 | 2026-10-08 18:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 241.3 |
| e69fab32-f00e-386a-8faf-a4cd83825fcd | -2.572 | -56.1646 | 2026-10-08 18:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 139.8 |
| 428b3744-23b0-356d-a6d7-537fb28eaba2 | -11.6387 | -43.5929 | 2026-10-08 18:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 394.0 |
| 9679c432-3400-3a13-b202-6189718794c8 | -3.8598 | -44.1504 | 2026-10-08 18:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 154.7 |
| 160a2e8b-1703-39ff-850a-f481fe21b21a | -8.2176 | -46.4068 | 2026-10-08 18:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 84ffe3a0-0ae0-3ec7-973e-f7f12e31a069 | -6.3283 | -55.3276 | 2026-10-08 18:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 107.9 |
| dcb707c8-320b-30e6-93eb-58a26595f8a3 | -5.6136 | -44.3647 | 2026-10-08 18:50:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 900c44c7-b9a4-3b43-b3a5-5b56dcab85ae | -2.8163 | -54.133 | 2026-10-08 18:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 5a88d85a-edfc-33af-82fc-33a787b08e5f | -2.8434 | -57.4696 | 2026-10-08 18:50:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 90.6 |
| e8a9eeda-86a5-3d37-815d-858fef48cb40 | -12.2123 | -44.7457 | 2026-10-08 18:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| e173b4e0-dbea-30f0-acba-84a582e5495e | -2.8712 | -54.1719 | 2026-10-08 18:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 632f0fcd-b0a4-3d88-859b-e8d99a91d589 | -2.8346 | -54.1326 | 2026-10-08 18:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 173.7 |
| 972c62d2-ec50-3944-9d4b-8e39ea982f1e | -4.7589 | -55.6516 | 2026-10-08 18:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 224f37eb-59bf-36cb-8f76-fa79117e12f6 | -7.4886 | -42.8295 | 2026-10-08 18:50:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 93.9 |
| c4a5716d-3f39-39da-a142-4e8e3301d5d8 | -3.1951 | -42.9538 | 2026-10-08 18:50:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 695b9de9-16f0-341e-b0c5-3af75cb5b844 | -6.4764 | -55.3004 | 2026-10-08 18:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 219.5 |
| ecf7cb1a-19c8-3d51-a12b-5e92e385568c | -3.7809 | -41.7913 | 2026-10-08 18:50:00 | GOES-19 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 110.0 |
| 7f7bab0a-24b0-3f3c-906d-526a504d8a88 | -5.9835 | -40.9367 | 2026-10-08 18:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 59.9 |
| 4758c7fc-e873-3280-988a-9b24aabbede2 | -5.3951 | -45.9194 | 2026-10-08 18:50:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 16a666e3-de5d-378f-a4e6-afe2aa0fb0ff | -2.8571 | -59.2641 | 2026-10-08 18:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 93fa3da0-2c71-31b0-b02d-e862296e8244 | -2.8896 | -54.1715 | 2026-10-08 18:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 495daa5e-a573-3c67-a8df-3adf6bea4c5d | -10.9384 | -45.3916 | 2026-10-08 18:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 3f8fa184-4d21-3066-868f-5d2c114866c5 | -2.4942 | -58.0768 | 2026-10-08 18:50:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 118.5 |
| e95be821-3279-3c2e-a6cc-de8ed9de6591 | -3.8198 | -44.6095 | 2026-10-08 18:50:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| be9077c5-367b-38a3-8b8f-f0a0e5b2f0e6 | -6.8907 | -45.8988 | 2026-10-08 18:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 28b07436-e934-386d-b1da-1772fc97d8b7 | -3.2945 | -54.0006 | 2026-10-08 18:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 105.3 |
| ac657bb7-e73b-381d-a2ce-977100ad3889 | -13.885 | -44.1365 | 2026-10-08 18:50:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 301.7 |
| 9b2744f5-9493-34e1-9fc6-d2b120c7943e | -5.4142 | -45.8734 | 2026-10-08 18:50:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 933f814f-22ca-3269-9d58-554f75ef2ce2 | -3.3912 | -58.0017 | 2026-10-08 18:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 182235e8-09b3-3443-acd2-aed53252009d | -3.8383 | -55.9774 | 2026-10-08 18:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 6a41eb65-fca9-3e32-83a4-2fee190d1365 | -5.6935 | -53.4464 | 2026-10-08 18:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 203.4 |
| 0ed544c0-4c1e-32aa-8af1-82222c54a5bf | -12.2316 | -44.7427 | 2026-10-08 18:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 164.7 |
| 9c56ee6c-cb71-3ec6-a089-35f3248290cf | -16.9851 | -41.2252 | 2026-10-08 18:50:00 | GOES-19 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 91.5 |
| d987619c-2821-3e2c-9e7c-652752ee7346 | -6.1427 | -47.9649 | 2026-10-08 18:50:00 | GOES-19 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 8a492418-eb6a-312d-941b-79bfcea6bc8c | -3.1298 | -53.7834 | 2026-10-08 18:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |


[Clique aqui para ver as próximas entradas](README398.md)
