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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b64b60d-7abc-36bc-9008-e16563aeb4e1 | -13.07118 | -56.8702 | 2025-08-06 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b94d926-b7e0-3171-be09-0ac5452da72a | -13.05585 | -56.86101 | 2025-08-06 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| abc3eaaa-76a4-3cd4-888e-b35067385e78 | -13.07577 | -56.86297 | 2025-08-06 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| a995793b-3d3f-3089-a0b3-8fef4c1545b5 | -13.07175 | -56.86633 | 2025-08-06 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 115bac2a-e1fa-3e0a-a8f8-e9b7a5fb7446 | -13.05527 | -56.86489 | 2025-08-06 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 22364077-5c74-347a-aa84-d4e5f7794e23 | -17.83074 | -55.10186 | 2025-08-06 05:14:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 35e578a9-f1b2-3be2-bfe7-ee28bfe70a80 | -13.05411 | -56.87264 | 2025-08-06 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 712279d3-d469-39cc-b9eb-595c7e1f6267 | -13.04721 | -56.87155 | 2025-08-06 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63e5d7d9-01e5-39f9-b8f1-c28b18d4d6df | -13.06371 | -56.87304 | 2025-08-06 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10d42c54-ae33-3e94-a766-7aee2299677e | -13.05814 | -56.8693 | 2025-08-06 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d6630c3-a778-3092-aa25-7e3572833d06 | -13.06427 | -56.86917 | 2025-08-06 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7824e54-5b68-3c66-a11b-08eeede06daf | -16.34129 | -50.34643 | 2025-08-06 05:14:00 | NOAA-21 | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a056a962-07d9-3f36-87fc-873002a57c04 | -21.07393 | -49.99442 | 2025-08-06 05:14:00 | NOAA-21 | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1459a62a-ff1a-3d7d-bb2a-c5941df71584 | -13.06218 | -56.86596 | 2025-08-06 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5efc97a0-7a54-3f5a-8255-3be520a6fba7 | -15.66416 | -53.60889 | 2025-08-06 05:14:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| beeadb2b-ee8a-3677-9c82-b5aaf62f49dd | -16.71622 | -49.45235 | 2025-08-06 05:14:00 | NOAA-21 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e3a09b54-e1e5-3571-a560-9595bae11bca | -16.34629 | -50.35038 | 2025-08-06 05:14:00 | NOAA-21 | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e973c01-b81c-3c79-9746-44672fcdfbe0 | -13.05124 | -56.86823 | 2025-08-06 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1bb07c27-724f-3ea2-a93d-05f4d8ca8b80 | -13.07464 | -56.87073 | 2025-08-06 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91286e9e-a040-3f92-800e-8b47e343f943 | -13.06276 | -56.86208 | 2025-08-06 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 183f1a65-8f21-3bbf-8d79-3f24a4a77b6e | -12.43953 | -63.69973 | 2025-08-06 05:14:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6eda3543-7fdc-338e-a35d-c99df3df8812 | -13.06505 | -56.87037 | 2025-08-06 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03e09af2-9d2c-34cc-a766-4beb716b12c3 | -16.33555 | -50.34908 | 2025-08-06 05:14:00 | NOAA-21 | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b567aa2b-70bc-37a8-aef8-866919c9138d | -13.06102 | -56.87371 | 2025-08-06 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8351105-aab5-3314-8cfd-69bcab2305dc | -13.93643 | -54.06704 | 2025-08-06 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73b30753-350c-3d2e-807b-295690acf242 | -15.65988 | -53.60829 | 2025-08-06 05:14:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77175ca4-ddc9-3acb-bf22-db0d88bcc902 | -21.0744 | -49.99131 | 2025-08-06 05:14:00 | NOAA-21 | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 16a915f3-8e80-3aa5-8d40-c0394bcc3080 | -17.83474 | -55.10244 | 2025-08-06 05:14:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 98e1f25a-ee2b-3873-a67a-22740ef24379 | -13.04779 | -56.86767 | 2025-08-06 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89d72c0f-2d1c-3d03-b583-a5dd9d2649c1 | -13.06447 | -56.87423 | 2025-08-06 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e25a7d6-8dc5-30b1-927b-ba34613ae79c | -19.84577 | -51.20324 | 2025-08-06 05:14:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 21e07c82-e77e-3e95-b0b1-99773d750797 | -21.01783 | -49.90133 | 2025-08-06 05:14:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 056c25c8-27a8-3acc-8f64-0cc1fcc2a2d9 | -13.06773 | -56.86969 | 2025-08-06 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f07c891-66b0-32b7-93cf-db48e914c05d | -13.0616 | -56.86984 | 2025-08-06 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8508a56-3031-3f8a-8a18-32512d922516 | -14.02296 | -54.07153 | 2025-08-06 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cb74e444-e471-3c8f-84d0-4305ff73d3fd | -13.06483 | -56.86528 | 2025-08-06 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 53ca0bce-fbf4-3e50-9ed1-0564f200fbba | -13.05239 | -56.86047 | 2025-08-06 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d570aa1-7bbd-3d4c-a112-7ea2d4c23664 | -13.0654 | -56.8614 | 2025-08-06 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 545ab57c-1267-3104-b4bf-8d5908a0b754 | -13.05066 | -56.87209 | 2025-08-06 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8cd6556c-8378-3534-9df1-25d5b397876c | -13.05872 | -56.86543 | 2025-08-06 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5ae58206-54f1-36ff-b38d-0a86006e02bc | -13.06563 | -56.86649 | 2025-08-06 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 91760263-fb65-3dd6-9d6f-8b6e80731329 | -20.22584 | -50.91732 | 2025-08-06 05:14:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 70a7d433-ef82-3a45-a6ee-a1c82ca3b6dd | -13.06885 | -56.86193 | 2025-08-06 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 249d37a5-204c-3bb6-8b48-6bc114d1e583 | -15.2115 | -55.64627 | 2025-08-06 05:14:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 019c68a7-46a0-34d0-8e0b-057e04e229f2 | -13.05182 | -56.86435 | 2025-08-06 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61731703-e561-3dc1-ae9b-a915a066f6e3 | -13.0731 | -56.8527 | 2025-08-06 05:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 24ee6a43-e8fa-3688-b1f4-2ea8615ff906 | -11.9207 | -44.9525 | 2025-08-06 05:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 204ab79c-cbb7-3e97-9a90-7f32038c9d1f | -13.0728 | -56.8729 | 2025-08-06 05:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 1bc067cd-807f-3f7b-8c6a-3042a23441f6 | -8.9213 | -60.7489 | 2025-08-06 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 24f7c8d2-626a-3a3f-976a-f5c531410345 | -8.9028 | -60.7498 | 2025-08-06 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 9416bf33-62ab-3b08-a4c2-05306c887383 | -11.9015 | -44.9554 | 2025-08-06 05:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 2fb20394-58a9-3993-be70-fe7a40997e20 | -8.9213 | -60.7489 | 2025-08-06 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 84dc9bbd-5fcf-3006-ae7b-04eef833ba98 | -18.3823 | -52.1029 | 2025-08-06 05:30:00 | GOES-19 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 56.9 |
| ad30635a-afc5-322c-8c94-fbcf725a7d4c | -8.9215 | -60.7297 | 2025-08-06 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.4 |
| f6562259-f79d-3605-bcdc-5d6943ebac5e | -18.3818 | -52.1248 | 2025-08-06 05:30:00 | GOES-19 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 102.3 |
| e3c59319-0844-3d24-8c2b-1f1df6a34064 | -3.0384 | -59.9108 | 2025-08-06 05:30:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| e27104cd-b840-3f47-a487-2c1d48717eab | -18.4018 | -52.1214 | 2025-08-06 05:30:00 | GOES-19 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 7057d653-a6df-3b55-a484-c38b613c2a62 | -3.0566 | -59.9105 | 2025-08-06 05:30:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 6bcdda6d-b766-3a9a-a364-6ab6aa626ada | -3.23659 | -60.19736 | 2025-08-06 05:36:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 294b076d-1d5c-33d2-b857-3a9f98f677a0 | 1.6907 | -61.07409 | 2025-08-06 05:36:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1bcf4d8-25bc-3d7a-ae78-df417d40f07d | -2.165 | -60.01789 | 2025-08-06 05:36:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9271626a-aacf-397a-b278-1e0933cd85f2 | -3.04211 | -59.91412 | 2025-08-06 05:36:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cdb8b3bd-f4c9-3eb3-8b84-0cb02eaffd0b | 1.69125 | -61.07757 | 2025-08-06 05:36:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f01d39cd-0430-3f6a-b541-d0309ba69f4d | 0.64836 | -59.74296 | 2025-08-06 05:36:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1168a254-b47f-39cf-aa71-50c2a2d34e51 | 1.68792 | -61.07808 | 2025-08-06 05:36:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 75d88251-e6ef-3fca-b86a-25b601f00221 | 1.68737 | -61.07461 | 2025-08-06 05:36:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30304292-35c3-3252-b06d-25b85f73d829 | -3.0457 | -59.91469 | 2025-08-06 05:36:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 174.0 |
| 7acf2f47-a620-3f17-ad81-0e52ed3b8b6a | -3.04274 | -59.91003 | 2025-08-06 05:36:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dfacf0f4-458d-321a-913f-948efa3e06ca | 0.65184 | -59.74242 | 2025-08-06 05:36:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0a20438-25f8-30c1-8320-feae40fefe88 | -7.59818 | -55.19927 | 2025-08-06 05:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ba620138-3557-3465-ac81-eee4cc8a7ee7 | -7.01734 | -59.83373 | 2025-08-06 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.2 |
| f28d0c8e-8a83-30e6-9b32-5eccda0b00ef | -9.47459 | -57.8532 | 2025-08-06 05:38:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba5f0e03-43ec-34ad-8aff-090afbdb04d7 | -8.92301 | -60.56646 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e8bcd297-f438-32d3-ac94-8a0a0ed8c5e7 | -8.91969 | -60.74073 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 40dff2b3-3b94-3047-8412-f12198615268 | -8.91142 | -60.54206 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 26.9 |
| d7ce5871-e4bb-3610-b8f7-96dbe598f7ee | -8.91405 | -60.60135 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 68a9fbb4-85e5-3462-b0b1-0c4ba7272da0 | -8.92582 | -60.5986 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 753cb2c2-7378-3e9a-8508-33d594842091 | -8.92061 | -60.55704 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a2d37baf-354c-38cc-b699-688d4483f6a5 | -6.2724 | -53.63056 | 2025-08-06 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6fa5f24c-17d1-3a1e-ad64-5dd5261c1aad | -8.91995 | -60.56148 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5546e26c-8664-340a-a0f3-547ccdfc0c41 | -8.9217 | -60.57529 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3f3fb1ba-33bb-34cd-a2ca-121f9bd9d32c | -8.92212 | -60.59803 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 451b63b0-50f9-398c-aa14-7bffc98e5871 | -8.90751 | -60.56861 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 693684c0-7a76-3da4-8a85-5a0ddc6ae9dd | -8.91449 | -60.54705 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 2d4700a2-1c7f-3e38-bdb3-21631bde0a7f | -9.18137 | -60.82727 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3cc16a83-453b-3e8a-b4af-000fad5bd8f1 | -8.92433 | -60.55761 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c2ff89e-b0f9-37f7-a624-c04b1e9cd1f8 | -9.47182 | -57.8507 | 2025-08-06 05:38:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5289f49f-e82d-3827-9ba4-0dd4dbd199b0 | -8.92542 | -60.57585 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8abfd471-13d0-36d0-bccc-f5d8642b9a98 | -8.91384 | -60.55148 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 87de7d43-d829-3cd4-b382-3534fcd80215 | -11.32382 | -55.22375 | 2025-08-06 05:38:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4850ee4-7f68-38bd-abe2-28fe7c385489 | -8.91514 | -60.54263 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 837f746f-f34f-380a-813e-9f59e201c5c8 | -8.90555 | -60.58193 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 30.2 |
| edc55721-85a8-32c7-a1ce-92708f300228 | -8.91362 | -60.57861 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d8199b1a-c598-33ce-b5a4-bdea597bd60f | -8.90729 | -60.59581 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 101.6 |
| a49ffe04-99b4-3d9d-a038-09a161ad7332 | -8.90881 | -60.55979 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 36f4591a-d6eb-3d1e-b635-114d0e16c8fb | -8.92344 | -60.58916 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d07eb554-ced5-3a9e-9e52-7532cec13589 | -8.90249 | -60.57693 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 83b93a39-c5b5-3fe5-a21f-251a9fa786b0 | -8.9051 | -60.55923 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| fdff77b5-cef7-39d9-ac83-5572c8b700d8 | -10.2378 | -56.76817 | 2025-08-06 05:38:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d9cc081-c497-3e76-90b9-5f252a506c36 | -8.90184 | -60.58138 | 2025-08-06 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README27.md)
