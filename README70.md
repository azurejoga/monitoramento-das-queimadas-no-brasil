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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72519bd1-c7c6-3771-a85c-bee1b4603a70 | -3.92123 | -56.09864 | 2024-10-14 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 313756d8-bbdd-3418-a492-620c691100d4 | -3.91699 | -56.09793 | 2024-10-14 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 165454b5-e731-3c80-8480-de7b71086537 | -3.91376 | -56.11775 | 2024-10-14 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b0286fa-f867-33e0-b8ad-a3ba4fa5e47e | -3.91312 | -56.12169 | 2024-10-14 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 617fc17c-3478-3475-80ab-86a72b0ad931 | -3.8936 | -55.82023 | 2024-10-14 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13a57fd9-35a4-35e9-bf4a-e2f46ea02b14 | -3.88207 | -55.83786 | 2024-10-14 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a569f848-edf5-30de-bdf5-83bcd57575df | -3.88145 | -55.83875 | 2024-10-14 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 322d7732-838d-3132-b8e4-502da45ca897 | -3.87924 | -55.77262 | 2024-10-14 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f48b377f-21b3-3774-aa19-0d701f1a417b | -3.87728 | -55.83799 | 2024-10-14 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4effdfc8-a786-3637-abb4-807a6b1b7a95 | -3.87507 | -55.77196 | 2024-10-14 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f00bb5c1-f91b-3988-a4e7-1360d886c97b | -3.87447 | -55.77568 | 2024-10-14 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8a3f45a0-433e-3df0-9640-96afb4242099 | -3.87091 | -55.7713 | 2024-10-14 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0a4d32b4-14f5-3a9c-abac-bccd682909c6 | -3.87031 | -55.77501 | 2024-10-14 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8556ed36-6111-329a-a8b3-fa96aa10b28b | -3.85293 | -55.80301 | 2024-10-14 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66dc52e3-1ad3-3578-89e7-6ce7c6a8cd93 | -3.84877 | -55.80227 | 2024-10-14 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25db24e7-f337-3d59-8f43-1000f984062c | -3.83272 | -55.98056 | 2024-10-14 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 84f719ee-2cd1-3841-9c4b-0fa41bf4e637 | -3.83209 | -55.98447 | 2024-10-14 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| ac156875-95db-327d-81bf-3a1e4546e4a8 | -3.83146 | -55.98837 | 2024-10-14 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 16c5ab3e-f5f8-393c-b6ff-a052c3c6fd02 | -3.82786 | -55.98379 | 2024-10-14 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 7ba8822f-1c4f-3a5d-9b90-dd669ae07e34 | -3.82723 | -55.9877 | 2024-10-14 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| f8e3ef32-687d-3dfc-9721-b68974f64a65 | -3.68434 | -55.96149 | 2024-10-14 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7dc935cf-cfd0-3235-8767-06b8e0c77186 | -2.94159 | -57.13936 | 2024-10-14 04:44:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2fb24c5-cfe7-3d88-8da3-21612e625989 | -3.67926 | -57.01089 | 2024-10-14 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 848acda1-7953-3a49-a8a8-37893ed14108 | -9.19733 | -47.56126 | 2024-10-14 04:44:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 380e1eeb-9c6e-3a6b-ba0a-72c00e86e215 | -9.82331 | -45.04908 | 2024-10-14 04:44:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7327046-bf11-306b-8387-882baba0272c | -7.08928 | -42.6584 | 2024-10-14 04:44:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 680c1294-8518-37fe-93c8-4e469c428a4f | -7.08377 | -42.66061 | 2024-10-14 04:44:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fde0ce6b-78f0-3a55-9ea5-ea5182aff1d0 | -7.0816 | -42.63921 | 2024-10-14 04:44:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 614d1964-66f1-3a77-b1c3-9720a867d31e | -7.07866 | -42.65994 | 2024-10-14 04:44:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c6beb5e9-6853-3f86-a22b-f77028ae223d | -7.07651 | -42.63844 | 2024-10-14 04:44:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1fd9c8b5-883c-3fcb-9f04-38945a8f4eb3 | -7.07398 | -42.65633 | 2024-10-14 04:44:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 66f59445-f1bd-3f3b-a01e-ec84afe3153b | -9.17257 | -45.58581 | 2024-10-14 04:44:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 81b6af69-0645-3e5c-9440-13ee021079e7 | -4.04521 | -43.04312 | 2024-10-14 04:44:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5605fbd0-535e-3988-a588-e705aff473e7 | -4.04467 | -43.0402 | 2024-10-14 04:44:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f8ac74f-5bde-3f46-a510-349a0fcb3699 | -4.04449 | -43.04816 | 2024-10-14 04:44:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a96dfe6b-d4a5-3334-bf2c-03d029bde3d7 | -4.04391 | -43.04522 | 2024-10-14 04:44:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3963ec9c-c3cf-3031-9d77-4c937044997d | -4.04048 | -43.04238 | 2024-10-14 04:44:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2e8b4c5a-6672-31c3-b751-b66fb346305c | -4.03994 | -43.03943 | 2024-10-14 04:44:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cdfc30cb-751b-3454-8e0d-2375529c27d0 | -4.03975 | -43.04743 | 2024-10-14 04:44:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f2848bf0-f903-3f61-b487-0f8ed7010e65 | -4.03917 | -43.04451 | 2024-10-14 04:44:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2b9c53a0-d3a9-3159-b2de-55e5b01d79c4 | -4.03841 | -43.04951 | 2024-10-14 04:44:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ea9e1ea9-6c1d-3622-82cc-984cb1e09b9f | -3.31029 | -42.83628 | 2024-10-14 04:44:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| b0e1a58e-3265-3334-863a-b01c2536d796 | -6.90596 | -43.49227 | 2024-10-14 04:44:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 420082ce-b7e5-3d7a-bdf9-81249c0983b8 | -6.90522 | -43.49751 | 2024-10-14 04:44:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4651dd11-8589-3ceb-a6d9-8b50dcbef848 | -6.72599 | -43.56132 | 2024-10-14 04:44:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 79a162f4-794c-3608-be59-5453b46a53f0 | -10.04377 | -44.21564 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9be14113-4539-3baf-8a12-bc155dcd9e1e | -10.04037 | -44.20478 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0c0f6a93-a539-3441-8ff8-62f0def8b54c | -6.4527 | -43.93654 | 2024-10-14 04:44:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a7f2507d-89db-3aa9-8578-238180f62c42 | -6.6783 | -43.65797 | 2024-10-14 04:44:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bb94256d-ab70-341c-bc9a-832ad36e866f | -6.65766 | -43.96979 | 2024-10-14 04:44:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 254a4d91-2aee-3e07-9179-a42bdee68c2a | -6.65371 | -43.96439 | 2024-10-14 04:44:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e16fade4-e8da-3d8f-a735-364d824a615a | -6.64928 | -43.92931 | 2024-10-14 04:44:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31407f9a-b6b7-3536-88fd-453f4e726e92 | -6.64908 | -43.96373 | 2024-10-14 04:44:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32394fa9-521e-33fb-83bb-846a63341fca | -6.64859 | -43.93416 | 2024-10-14 04:44:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e78ca13f-1804-31c4-9889-4c45340c711d | -6.64789 | -43.93902 | 2024-10-14 04:44:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 327ab9b3-9683-33c9-8b03-002bad06d14a | -6.23691 | -43.47541 | 2024-10-14 04:44:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2fa3cf19-7e79-352a-8e88-11d5e9e9a828 | -6.2362 | -43.48056 | 2024-10-14 04:44:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 68905795-5491-34a0-b6b1-db19f46d2311 | -6.23116 | -43.51664 | 2024-10-14 04:44:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b0c3b645-68a2-345d-a6f3-4947915e592b | -6.231 | -43.51556 | 2024-10-14 04:44:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 64bafaa1-b89e-3d4d-99b7-276b84d034e0 | -6.2271 | -43.51109 | 2024-10-14 04:44:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5cca7b1d-3a0d-37b2-bf20-cf175728150c | -5.99162 | -43.99593 | 2024-10-14 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01de564b-2a50-3b3f-a03c-f6af476676d5 | -5.68654 | -43.75183 | 2024-10-14 04:44:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa764a23-d90c-3516-bacb-63f7b4d3ab9f | -3.41392 | -43.34793 | 2024-10-14 04:44:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8b7b98ec-3b3f-3471-95cc-30448fa8cd43 | -4.43356 | -43.92754 | 2024-10-14 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cdad6680-6cbc-345f-bb65-62f93ce1183a | -5.09939 | -43.81507 | 2024-10-14 04:44:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 095dbafb-08f3-3869-8e8c-44c8f17fd69f | -7.93576 | -44.52097 | 2024-10-14 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9247aed3-cdb7-375f-b84b-04ae55f58c2a | -7.93239 | -44.51197 | 2024-10-14 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 69a91c4e-e2dd-3521-96db-c635ead9f44c | -7.9318 | -44.51617 | 2024-10-14 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 63c3c664-eaaa-3494-8a5a-c4620a46124c | -7.92725 | -44.51564 | 2024-10-14 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e16b3b85-c067-3b90-afe7-a25c26690bf7 | -7.9227 | -44.51506 | 2024-10-14 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a8c014f4-c1c6-3b0a-8ffd-ffda8d75ed31 | -10.07795 | -44.21512 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bb9f6344-8aff-395c-b264-cbc64095030a | -10.06824 | -44.2504 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 36dd7e99-50cd-30cb-bbfc-e0d199f709ea | -10.06753 | -44.25554 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 4de9d8cd-7d87-3b33-bb1c-58a3863ae4dd | -6.22698 | -43.50998 | 2024-10-14 04:44:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| babbd61e-368b-39df-a353-93fa8fb1b623 | -6.21283 | -43.50739 | 2024-10-14 04:44:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c707f518-4bbb-3498-8712-7655e70ea213 | -6.21216 | -43.51197 | 2024-10-14 04:44:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80efc92e-f01b-3ded-89c4-a8eb5b4d7c90 | -6.22573 | -43.52089 | 2024-10-14 04:44:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bb54f009-b3dd-379b-8a25-26efd6f85c0b | -6.22552 | -43.51986 | 2024-10-14 04:44:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e3d0c549-334b-3e66-9001-bb6ddbaf5d3f | -6.22031 | -43.52515 | 2024-10-14 04:44:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8690c8c0-d11f-3aa9-95a9-6a4b7672faa5 | -6.21624 | -43.51961 | 2024-10-14 04:44:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0967ee30-04ef-3edd-b4cd-92402bb32a14 | -4.37938 | -37.903 | 2024-10-14 04:44:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 48adff49-ad50-3b1f-955e-3bed1ad9a468 | -4.37853 | -37.90878 | 2024-10-14 04:44:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 1889f565-4dcf-3c90-9d23-ca3d196ab2fe | -4.37687 | -37.89983 | 2024-10-14 04:44:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 0a858d11-511a-3070-b0dd-78f963d032cf | -4.37607 | -37.90561 | 2024-10-14 04:44:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| c18a9951-d742-3ef1-aa13-cdc26b7fa1e2 | -4.3727 | -37.90207 | 2024-10-14 04:44:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 179a0f8c-8a05-34d4-a8a8-b75b05b50bc9 | -4.37186 | -37.90783 | 2024-10-14 04:44:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| d29f8b76-270f-309d-b15c-d6dff6b8e151 | -7.51778 | -40.51237 | 2024-10-14 04:44:00 | NPP-375D | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fabb9260-3e68-330c-b2e6-b95234ce5387 | -7.51715 | -40.5171 | 2024-10-14 04:44:00 | NPP-375D | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b6b45588-8e2b-3a5e-b1c1-81ede874db4c | -7.51428 | -40.51469 | 2024-10-14 04:44:00 | NPP-375D | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ae35bb0e-db84-3d3b-a0d9-6792adda8e0b | -7.51361 | -40.51952 | 2024-10-14 04:44:00 | NPP-375D | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c7d69860-10c2-3751-817f-a7dbfad8c49b | -8.37724 | -40.26848 | 2024-10-14 04:44:00 | NPP-375D | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 891ca39f-ca97-3d45-87a8-6a4542e834b5 | -5.12796 | -41.70469 | 2024-10-14 04:44:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3e9d34df-405f-3d57-91a8-cb354e2058a7 | -5.1275 | -41.70794 | 2024-10-14 04:44:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5b4de9dd-fb97-3bf6-b1e0-df57e9ca4864 | -5.12589 | -41.68119 | 2024-10-14 04:44:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 958ea9e5-5f2a-3d7d-b447-f5844b118b65 | -5.12543 | -41.68446 | 2024-10-14 04:44:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| bdcbadb4-9827-33eb-b1d4-3e23e772b9cf | -5.12175 | -41.71045 | 2024-10-14 04:44:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| c37f161e-68c5-321f-b0c8-87f639ff6c2a | -5.1213 | -41.71363 | 2024-10-14 04:44:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| fe3df2bd-adc3-3108-b59c-4668aaa4d102 | -5.12104 | -41.67731 | 2024-10-14 04:44:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ed0fb02a-5de4-3813-8e8d-88f520f1a0e6 | -5.12085 | -41.7168 | 2024-10-14 04:44:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 94188361-e131-3eb3-b5f3-648d23b6897d | -5.11574 | -41.67661 | 2024-10-14 04:44:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README71.md)
