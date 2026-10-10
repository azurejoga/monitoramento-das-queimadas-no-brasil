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

## Dados Diários - Página 128

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0185995-bbb7-3614-943f-6ca9e0f94042 | -3.6418 | -55.49223 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60c2cd0d-9a52-330c-81aa-0703afcb49db | -3.51132 | -54.54502 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3476c249-09f0-3461-9ef9-b1150f720c53 | -3.187 | -58.63963 | 2026-10-10 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eef90495-5532-32c8-bce8-af7c12e72471 | -5.86005 | -55.70449 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c06c3793-097e-3027-9fc6-2c9dec9b6531 | -5.95104 | -55.35311 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ee8a8cd8-bb96-3b46-bb0f-a8865cf45157 | -7.21606 | -55.07096 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 25583a00-a155-3cb6-bddd-426aef698018 | -1.1981 | -55.6859 | 2026-10-10 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 53348e33-e35f-3408-8632-148840ca8c75 | -3.179 | -54.75093 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5a800ce-a503-3d4a-b48b-a9bb73819b13 | -2.52054 | -56.27164 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ec3b91d8-2fd0-3c67-8e37-5c64eec7e3aa | -3.31021 | -54.67424 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 17e05afb-7005-3f5e-ab22-1647389fd22b | -3.88452 | -55.99056 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| df8cd342-30d7-3426-bf4e-82ca7b31ebed | -3.72106 | -57.14145 | 2026-10-10 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 838f2cc3-b11a-3293-9227-42a15ec71534 | -3.311 | -54.03028 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac9bb48c-9a73-300c-99ac-9d975962c7df | -5.7889 | -53.80815 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2b48a22-5225-3fc1-a283-c41f20834047 | -6.68264 | -55.09272 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c7698d5-b4f9-3efe-9b02-ff703ae4cffc | -3.30027 | -53.71099 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 284ae2e3-3ceb-3b48-a7f9-659f6bcd2e6d | -3.73132 | -57.14753 | 2026-10-10 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 696b6c3c-bf5a-31b3-b5a5-4056e9347cc1 | -1.46034 | -54.74747 | 2026-10-10 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b51dcffc-0e1a-3b6a-af55-aa01a0cd5f3a | -3.21788 | -54.29498 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 77da0964-5f34-3e19-b260-29501dd2d845 | -8.19751 | -45.74766 | 2026-10-10 05:04:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a6898e9d-40e9-3b10-96f2-f62ffd89a768 | -3.73824 | -52.24941 | 2026-10-10 05:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce927ae9-4b4e-36fd-92d2-c4bc1dfdb9d4 | -3.03454 | -53.95129 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be5f401b-a1af-3df0-998d-0d81da2ad1f5 | -2.73823 | -54.10572 | 2026-10-10 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98f3c9a2-c646-3b7a-b8fd-f07d3224bc4f | -6.68319 | -55.08923 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f09a730c-18f2-3065-8ad0-87906af25e62 | -3.26592 | -54.24962 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69ab5584-5c88-3580-9884-c42aaf493bf8 | -3.57486 | -59.07515 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64f03579-6fae-3342-b675-3abfda9dd9e3 | -3.57633 | -54.71235 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 655e0527-ab39-37d6-a845-47e240351361 | -2.87695 | -56.6649 | 2026-10-10 05:04:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b76d5ebe-1904-33d2-96a6-840e62718fdf | -3.657 | -54.28981 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 284cd9ac-6c8b-3dd8-882a-c278c2b239a0 | -3.88677 | -52.19498 | 2026-10-10 05:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4fa32f61-1738-3d38-b8b2-79645764d582 | -3.03614 | -54.24143 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1801cd9a-62cb-3d40-9905-d68d38b52ef8 | -2.86701 | -54.87611 | 2026-10-10 05:04:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f888a69-09d5-3103-af2c-22a91b6ab883 | -6.15572 | -47.96275 | 2026-10-10 05:04:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9ec9652e-3ff2-3386-943a-a685c6440891 | -7.53405 | -45.31974 | 2026-10-10 05:04:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 759dcc1e-1369-3b88-b789-7045c867d2b0 | -3.45528 | -50.58981 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a73343c3-21a6-369d-bd5d-0392bb3fc0c6 | -2.48123 | -56.13194 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0fcb032c-52bc-3846-a892-0b5d012b415c | -3.95489 | -55.33672 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 953c6234-2649-3496-b18a-880e832a4821 | -3.60576 | -54.59146 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a229d5f0-3d11-3307-b16d-c5517924bbbf | -3.49692 | -54.61432 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c85b8788-8d27-3083-9178-8cf892165b2f | -4.5479 | -54.96658 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5cb11ce1-4380-372e-a82a-aa464420a1f4 | -3.16194 | -50.59438 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2fc13a52-9425-3d75-810b-75531a83ffc5 | -4.42943 | -47.54119 | 2026-10-10 05:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 83cff9ea-1674-3de9-ac0e-468a32787b44 | -2.84048 | -54.12573 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c667b203-6044-3dea-8736-2b01b540b48b | -3.48724 | -59.2063 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c02a3155-9b89-3672-8e9c-3b2d520e44e9 | -4.12493 | -54.25446 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 31d88b46-96e3-3f66-9f08-5cce5bf02f5f | -3.3488 | -50.48116 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8db054cc-05b9-3adf-b80c-23c7fb1011a5 | -7.18837 | -55.15935 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2e60477-33be-359a-bb8f-7fb391cd9865 | -7.22045 | -55.15018 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3820547-b4ae-34aa-ac05-decd155bf481 | -6.70632 | -58.71771 | 2026-10-10 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0052df9-72fb-30e4-a886-5aa759135a28 | -4.7448 | -57.48096 | 2026-10-10 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf68959b-bd50-3209-bfab-a5878dce6c66 | -3.30965 | -54.67773 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb9d7547-66d2-3904-87bd-01f8d61be6c6 | -4.8983 | -54.98709 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| faff0847-4d06-3897-abcf-416b88230a96 | -3.01337 | -51.01009 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d364025d-0c8f-380b-8345-8498fa3e787a | -3.25645 | -50.42562 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 81a6a832-faff-33ed-b945-3cd5412f8dc0 | -6.68097 | -55.10318 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c998c2a-1753-3915-9462-25cb0e1d06c7 | -2.24253 | -52.08547 | 2026-10-10 05:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4fd7b0a-2d48-386c-9e06-1fab99f0af3b | -1.92319 | -57.04484 | 2026-10-10 05:04:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0537a736-aa53-3937-bfe7-e97ed6b50d9e | -6.44709 | -55.28785 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e93a2ee-2039-3176-818a-ece3e5527435 | -3.54911 | -54.69007 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| feb378f7-765e-3850-92e5-e6f49cf71ab4 | -3.11128 | -53.79044 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d124ec5b-94d5-32c5-9a49-a3789424aa81 | -3.93121 | -55.72199 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d18d553-8a1e-3819-bb78-8eaa78a51f25 | -3.25156 | -54.29706 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40aeca57-1a0a-35a2-94a3-c2b6f323cad0 | -3.12835 | -54.1744 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7a83cc07-1554-310d-8b94-e087839dcbae | -6.13861 | -52.87885 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e4aee7f-172d-31a6-974f-89c52606836a | -7.02639 | -47.65755 | 2026-10-10 05:04:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 1e6a0e51-b6c7-32c0-83fd-b20fc926b7b9 | -1.65067 | -55.2026 | 2026-10-10 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3e6b3ae-0bf8-31d5-a811-e436f0843517 | -2.46947 | -56.58826 | 2026-10-10 05:04:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37de596e-a328-3b0f-830c-bfc599af508c | -4.34377 | -54.8017 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f21eafe-d699-314d-912d-9c72d086df24 | -3.84561 | -55.79659 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 577fe537-cc85-3030-8c20-a47b9771d8d9 | -2.98708 | -53.90855 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5885c010-587b-3878-96d9-2b6e1fc26c98 | -6.42776 | -55.26323 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7db832ce-f14c-3907-bc6f-d36696205599 | -4.1543 | -55.13665 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce613550-b21d-3342-8cd8-1422f1041a08 | -3.57966 | -54.71288 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4cf75bfc-055e-378c-aa17-6b9388079559 | -1.18504 | -54.1743 | 2026-10-10 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc5adc7e-3b40-339b-9d35-80a55b798eab | -2.34623 | -57.99386 | 2026-10-10 05:04:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3990110-b735-3896-b78a-4fda8ce92690 | -3.11288 | -54.16488 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ccb5c2e9-c2c1-3538-85d4-068ec6ccdf91 | -3.31597 | -54.04166 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ea38af8-74a5-3239-83c4-2b1c3e3521e5 | -4.93695 | -47.44629 | 2026-10-10 05:04:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 247e2911-d232-3a0a-97f4-5d18b0f1d460 | -2.52827 | -56.26878 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d73a96dc-49fe-3cf1-bd06-94828faf63f7 | -14.73901 | -48.22753 | 2026-10-10 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c81bf302-ff57-39ba-963b-097ae680ebd4 | -13.52346 | -47.42605 | 2026-10-10 05:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0ca4138-fc55-3da4-b7a7-b0a66956c9d8 | -13.10488 | -46.3537 | 2026-10-10 05:06:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4a1678ae-0eef-37ae-8ed5-4ef17cb50f7b | -13.37758 | -43.89001 | 2026-10-10 05:06:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 41370fff-58ed-3cf4-811e-da4e96b46dc1 | -13.63437 | -44.4202 | 2026-10-10 05:06:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 825cd213-e9ec-3179-b2a8-f8e9546f15b4 | -11.08644 | -44.12088 | 2026-10-10 05:06:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| caf5cae4-4dfc-3fd5-b218-26c7be588b45 | -9.93673 | -44.88657 | 2026-10-10 05:06:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5695f9a5-f108-31bc-9f03-570f7d1c5d05 | -13.64929 | -49.40739 | 2026-10-10 05:06:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 140b590e-2c81-3af7-a8c9-0fdc90822490 | -11.77459 | -45.50347 | 2026-10-10 05:06:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5eb1d481-c5f5-347f-be8a-dc5409e66b7a | -12.25161 | -44.43238 | 2026-10-10 05:06:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9f2f5f7a-f81b-362b-9f59-99955ef240d6 | -11.72776 | -46.74214 | 2026-10-10 05:06:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7325fa98-9840-38f7-a6b9-f5ffbcc756cb | -9.21442 | -45.65703 | 2026-10-10 05:06:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab39ab35-42f1-3c3b-bbc5-75728b973273 | -9.1121 | -45.82875 | 2026-10-10 05:06:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 930c852a-0606-3e7e-8846-5e30ccbbde5f | -7.91179 | -54.71253 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 54ed652c-7a64-388e-b105-f111a4636baf | -11.19574 | -44.88111 | 2026-10-10 05:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 276ba18b-8347-39a0-bd0f-c4c4f723987b | -12.72962 | -47.01598 | 2026-10-10 05:06:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83fc48e9-cae2-3a78-af55-7c872264a31e | -7.90187 | -54.71095 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c2264cb-5ed6-3728-b424-8110679602e8 | -8.1863 | -54.71787 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a907f9ed-b091-34bd-81d3-55a1608cdbcb | -12.30213 | -63.36336 | 2026-10-10 05:06:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b3fd9b90-8c21-3000-90e3-9211d29b74ca | -10.60468 | -60.48999 | 2026-10-10 05:06:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3a5ff602-3d7c-325a-a6fe-1d7860add448 | -10.61466 | -60.48063 | 2026-10-10 05:06:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README129.md)
