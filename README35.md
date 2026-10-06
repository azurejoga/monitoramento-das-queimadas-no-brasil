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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ccd878b-2585-3338-8c14-b1844f365904 | -17.90491 | -41.58535 | 2026-10-06 04:21:00 | NPP-375D | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 865e41dc-3392-3a55-bcac-e7037f890dca | -13.03046 | -43.12333 | 2026-10-06 04:21:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 23.5 |
| b90e70d4-d45f-3356-9f4a-e87158e937c3 | -17.72469 | -42.63686 | 2026-10-06 04:21:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f0528cbf-e28d-316f-84b5-4ca47e7181ca | -11.69151 | -43.67052 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06def04b-1603-3c9c-8d10-4fd56fa0964d | -16.6762 | -41.847 | 2026-10-06 04:21:00 | NPP-375D | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8237d28d-5384-39a4-9865-05d25f7361a6 | -18.53959 | -41.29966 | 2026-10-06 04:21:00 | NPP-375D | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| c5c04604-fced-380e-87c2-bc759844529e | -11.66988 | -43.63364 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6824be24-a448-31b7-a444-31ba8435fe22 | -11.8324 | -43.54277 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f51260e-adf0-3e29-9a0d-478f494d4c67 | -16.01189 | -43.60253 | 2026-10-06 04:21:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b28f5068-894e-3e0b-bf10-b8d3296e5a98 | -11.71456 | -43.42061 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b1f6f8d3-f755-39a4-8572-accd38725887 | -12.76645 | -44.87679 | 2026-10-06 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a4a0c1ef-c456-39bc-b290-d656fd00a355 | -12.63887 | -42.86283 | 2026-10-06 04:21:00 | NPP-375D | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7da7e4c8-0bc1-3dc5-968a-a7461614e845 | -12.19488 | -44.65297 | 2026-10-06 04:21:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fded06d9-41c4-3fe7-9595-abdc63bdc83c | -16.78894 | -43.90292 | 2026-10-06 04:21:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4869f033-61aa-3506-a829-66b9ebed2998 | -18.53743 | -41.30194 | 2026-10-06 04:21:00 | NPP-375D | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 2e9e1db0-bcc3-3d1f-8bc6-8b881a4e0c95 | -11.67266 | -43.63779 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5914308c-4587-3e85-b691-f1f101355af8 | -11.67531 | -43.66409 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97539c34-e06a-3b91-ba26-777dbadf0c6e | -12.08726 | -43.41261 | 2026-10-06 04:21:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b522564-fda2-3629-b224-09ac70a5e1ca | -12.6169 | -48.48218 | 2026-10-06 04:21:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a55edfd5-46b8-382c-a494-b3a66e0e05b4 | -18.02948 | -41.6657 | 2026-10-06 04:21:00 | NPP-375D | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 71822eb8-c363-3035-86cb-2f31be5fd9c2 | -11.8255 | -44.69432 | 2026-10-06 04:21:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 7be6ef43-1447-3e64-b55e-833af765a0b4 | -11.82741 | -43.53108 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 294e98d6-d4a5-38fa-a041-d0ea909efdc0 | -11.68816 | -43.66996 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9e66172-95e9-3f2b-81ec-3c154230ea4d | -11.67924 | -43.66106 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d56da27-0da2-3c11-a12a-75defd0b9e50 | -14.05419 | -44.29162 | 2026-10-06 04:21:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cd5cad8d-e682-36c7-a6fa-ee731f8a0893 | -14.80623 | -42.00825 | 2026-10-06 04:21:00 | NPP-375D | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 23154dfe-26a8-348c-9a73-e3fda53ec6e6 | -11.69093 | -43.67413 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c667c3b-70cb-392e-a727-1a7cd432e7f0 | -11.69035 | -43.67772 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4818ddc2-2140-36a7-9b24-925b8a13b35f | -11.79123 | -43.53281 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be8c1de1-9e08-3b5f-81b5-f0d24e44c338 | -12.76175 | -44.88382 | 2026-10-06 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46de901a-6fbb-3a1c-a67f-165d6bd82d09 | -11.67414 | -43.67128 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a9e6721-f5d7-38b4-81bf-18373927fa73 | -12.76582 | -44.8806 | 2026-10-06 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3dae8711-213e-3ede-9b1b-02135603a4b2 | -12.64276 | -42.85984 | 2026-10-06 04:21:00 | NPP-375D | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b1f9ac78-865b-37e6-98cb-53416efcee01 | -11.6848 | -43.66939 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf7bbcbe-fad2-3ea2-8054-9c87e9818d51 | -11.67692 | -43.67545 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73d615e4-8e13-34a6-a1a6-db04dc90d0a0 | -15.145 | -42.16068 | 2026-10-06 04:21:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b3b49805-acc7-33d3-86e0-022fa06c45a8 | -13.02713 | -43.12277 | 2026-10-06 04:21:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 23.5 |
| f570d591-0766-33af-b068-037f0f67da42 | -14.19615 | -44.36745 | 2026-10-06 04:21:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ac7e03b1-dc88-370e-b0b4-12bb7bae4489 | -11.53333 | -44.89126 | 2026-10-06 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5057e97-cbfd-3fc4-8358-5bf5f403c5b3 | -11.67473 | -43.66769 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 47b25a7e-4157-3bbe-87a6-76312c85581d | -3.4943 | -54.6367 | 2026-10-06 04:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| c904c11c-0be6-3914-befa-be4c20cde8f7 | -3.5127 | -54.6362 | 2026-10-06 04:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 1f6912a5-bd43-3d9a-ba09-9a5428bd5820 | -2.9449 | -54.13 | 2026-10-06 04:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 4321ab39-1f0d-38fc-b80c-ffc67e5964aa | -2.9448 | -54.1501 | 2026-10-06 04:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| fb5117e9-1479-3cdd-b6aa-deb7d726c312 | -3.4944 | -54.6167 | 2026-10-06 04:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| e44beaa5-7a49-397c-8582-a34cc3bec0ea | -3.6732 | -55.9425 | 2026-10-06 04:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| f263e266-a884-3376-8e74-a850dbaf1173 | -3.0731 | -54.2473 | 2026-10-06 04:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 376bfb3c-6960-39ed-807b-1d64d439a94d | -3.0732 | -54.2273 | 2026-10-06 04:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 406f1f61-4924-3f47-8e9a-06ae521de8e9 | -3.0548 | -54.2076 | 2026-10-06 04:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 8e30eae5-1183-36b2-adaa-a4edb34a7c7a | -2.9265 | -54.1305 | 2026-10-06 04:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 478115fb-65ae-3d8a-9240-f666ff497207 | -3.0375 | -53.8865 | 2026-10-06 04:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 95a0d0fb-c065-385b-9acc-af8fd99fc450 | -2.9816 | -54.1291 | 2026-10-06 04:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| ee2bab42-8a85-38ac-a3ac-0de8bce870e7 | -3.0917 | -54.1666 | 2026-10-06 04:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 4330bcd9-9c41-3bbd-96e2-78edf29853bc | -3.1115 | -53.7637 | 2026-10-06 04:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 81bf04e0-4e39-3078-b878-8793344e3c4a | -3.0932 | -53.7239 | 2026-10-06 04:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| d790b4d4-4c18-3963-9fe2-6e4319795549 | -3.0915 | -54.2469 | 2026-10-06 04:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 9f3d8837-872b-3d75-8dd8-5923ae6026c0 | -2.8714 | -54.1318 | 2026-10-06 04:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| f632e279-65f6-3282-8f8f-723e40716416 | -3.5128 | -54.6162 | 2026-10-06 04:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| c2ca5063-f671-3f5c-87a6-e49c2ad01f62 | -3.0 | -54.1287 | 2026-10-06 04:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 3a44a81c-b4a2-345e-87d9-605785d0ca9c | -3.0191 | -53.9071 | 2026-10-06 04:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 2bfa303d-0973-34e7-8d3e-daea933cc800 | -3.0192 | -53.887 | 2026-10-06 04:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| bff1aadb-11df-32bf-8d67-b6b5d637b35f | -2.8713 | -54.1518 | 2026-10-06 04:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 355d073d-202a-3fb1-b38d-1f02387d93fe | -3.0548 | -54.2277 | 2026-10-06 04:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| e14fc759-62fe-3f9e-b7ce-0808ce54b156 | -3.0734 | -54.167 | 2026-10-06 04:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| d2e78596-053d-3e96-9c36-575ed2e1d867 | 3.31879 | -51.3392 | 2026-10-06 04:36:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 67c42a14-34e2-3856-a101-def306cbc541 | 3.31936 | -51.34299 | 2026-10-06 04:36:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2082e694-253b-3de4-ac88-818ad7fb7ea2 | 3.32353 | -51.34235 | 2026-10-06 04:36:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 95f1bbdf-c811-3542-89dd-6d04894e380a | 3.51374 | -51.28318 | 2026-10-06 04:36:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96b22a66-26a8-312a-bfda-e1bad27a7fd2 | 3.51789 | -51.28254 | 2026-10-06 04:36:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73952d7c-f642-3c85-b65f-c585476b2a42 | -4.99514 | -42.42978 | 2026-10-06 04:38:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dfc302f5-7c61-30e4-a0b8-bcdaa98f72a8 | -2.06943 | -56.85842 | 2026-10-06 04:38:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 63e1eaf4-1869-33bc-9e21-5c54618395ab | -3.08366 | -54.16769 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b117d52a-2e85-323a-9650-cd19c94dafe0 | -3.07452 | -54.16615 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5953cff1-c99a-3839-8ef2-691463ac2765 | -2.93464 | -54.13039 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ec436afe-1ea8-36a7-806e-775919c428b5 | -3.07834 | -54.17151 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a9f708a-598f-36fe-917c-944169c1ec13 | -3.1292 | -53.71733 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6dcff06-7821-38a9-b3d1-d19942b3c0ed | -3.67534 | -55.94346 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 968e59b4-844b-376a-9a42-22b0e5606178 | -2.9468 | -54.14207 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2053d445-d8d1-3e60-97c3-3d8946a9c2d7 | -3.39154 | -44.48036 | 2026-10-06 04:38:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37f59ab2-a3d4-3cdd-96f2-c229a48d5af2 | -4.77478 | -50.80655 | 2026-10-06 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7ce64e9c-a92d-33c1-8436-2e4f1794331b | -3.96749 | -48.12342 | 2026-10-06 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8caae3c1-490d-3a98-82bc-812049d415c2 | -3.6697 | -55.94565 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 66c3202e-21ee-3cf9-aec8-6927278d30d4 | -3.11806 | -53.70214 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3fe53c9b-3030-393a-b0aa-9f5149682446 | -3.00463 | -54.13243 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 2c8bcdb0-8055-3a6c-8b50-b5ccc61d90d7 | -2.87344 | -54.15913 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b829d5ff-065a-3ec4-b1b3-56a2657005dd | -3.08149 | -54.23671 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a02993cf-4b67-3e0c-8647-a2c032efd4ab | -2.87397 | -54.1571 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5d34584d-f0d5-38b1-bb8e-97b1f6cc70cb | -3.11319 | -53.75944 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| daa0d3f4-21ba-33c5-9d93-8f727eafc518 | -3.23268 | -53.88575 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56833721-c26a-30fe-8e5b-5ccba18efce5 | -3.50412 | -54.60843 | 2026-10-06 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd66361f-d86d-3949-b9da-37e44fa6ad07 | -4.11241 | -49.07003 | 2026-10-06 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc7e3120-b9f1-343b-b83d-dfa049df0739 | -2.78097 | -57.67115 | 2026-10-06 04:38:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a58df32e-490c-3c0c-a45c-d24179226e4b | -3.08292 | -54.17224 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d50abd4-c1f6-3e89-9d10-8cd6773eeb42 | -4.11521 | -49.07418 | 2026-10-06 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22368b14-e92d-36f7-90b2-b6f8a6d034b9 | 0.8229 | -51.61668 | 2026-10-06 04:38:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d73862e-03c5-389f-b150-b70b19485123 | -3.27741 | -50.0336 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89aa5032-f0b9-349c-8eb8-36b783629e74 | -5.41572 | -44.35322 | 2026-10-06 04:38:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 301dfe42-890b-3c0f-a953-26e82b364706 | -3.49396 | -49.90498 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 12a2009d-a846-39c0-a3fb-320345973be3 | -3.16818 | -50.43555 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2eb9b8f3-d9f2-3b95-99ea-c452b9e5b53f | -3.10335 | -53.70865 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README36.md)
