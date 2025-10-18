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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 727fd385-fc1c-36af-88f3-3986df230bca | -0.90033 | -47.54495 | 2025-10-18 04:46:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 10a3647f-109c-3d10-b9e2-df08a4c97615 | 1.49611 | -56.05272 | 2025-10-18 04:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d730e363-4802-3445-97e2-0e04d6aba794 | 1.50438 | -56.06666 | 2025-10-18 04:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92ffeb99-c1e2-3bc6-a501-1b5e1e6bf95b | 2.02403 | -55.82926 | 2025-10-18 04:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d12f1fa4-1cba-3493-9454-364318a627e5 | 1.76099 | -55.98257 | 2025-10-18 04:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| cb9e5cc1-7568-3424-a2d6-ccb61a1dae6e | 0.97735 | -51.1849 | 2025-10-18 04:46:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b53bffe-f074-3109-9966-8ea0f49fe2ea | 0.98012 | -51.18094 | 2025-10-18 04:46:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b0f70e6-012c-3629-9f64-4244d4d8a3d3 | 1.74272 | -55.75668 | 2025-10-18 04:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bee2eb2c-2ebe-3368-bfec-033c9e708045 | -0.90334 | -47.5499 | 2025-10-18 04:46:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a1e8430-57cf-3e8c-8039-ef686f2768eb | 1.76589 | -55.93239 | 2025-10-18 04:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c5edfbe6-c765-3dcd-a769-145014ef5f2c | 1.00988 | -51.17631 | 2025-10-18 04:46:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79129d30-29ec-313e-b927-e824c0aec2fa | 1.50498 | -56.07042 | 2025-10-18 04:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3bac4d25-4ab3-32d9-9eed-c9bf82ec6aaf | -1.61309 | -46.66788 | 2025-10-18 04:46:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64e15823-866b-3ba1-ba9a-836f090cd6ee | -0.89964 | -47.54932 | 2025-10-18 04:46:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e98796f-7ae7-3e65-84c9-6cbe9243740e | -1.61703 | -46.66846 | 2025-10-18 04:46:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 872d6258-c4b2-361e-a732-4bc843b116f3 | 1.00983 | -51.19748 | 2025-10-18 04:46:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df919d48-b7eb-3868-8869-8fe578b9ca5e | 1.76884 | -55.92424 | 2025-10-18 04:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c0947b2-07d7-399b-bfae-332c13a29d9b | 2.05097 | -55.73145 | 2025-10-18 04:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11be496c-5e0d-3d58-a14b-55e95cb1a5f9 | 1.77173 | -55.94282 | 2025-10-18 04:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8a94d066-b76e-35ae-ae76-020a466e602d | 0.69139 | -51.4628 | 2025-10-18 04:46:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e3210a5e-32f9-357b-82c2-485a83b5d102 | 1.73921 | -55.76092 | 2025-10-18 04:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0446eb5-3907-34bd-a53f-2cc8ecad73a8 | -0.90103 | -47.54058 | 2025-10-18 04:46:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 238afcf3-d620-3002-b681-3e8353b663e0 | 2.02104 | -55.83731 | 2025-10-18 04:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| beb742fa-9078-38aa-bd7d-b94973a4bf8d | 0.99112 | -51.18628 | 2025-10-18 04:46:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16e7b9ca-451a-3fec-b337-f5eda63b1607 | 1.76486 | -55.7384 | 2025-10-18 04:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34dab2f2-1032-324f-8425-579a969e8c44 | 1.75926 | -55.97134 | 2025-10-18 04:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ba9fdfbe-7398-31ab-9ee1-c5de331bd19e | 1.25306 | -53.07494 | 2025-10-18 04:46:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9584487b-3190-3a51-8e13-327787dafbb5 | 1.76837 | -55.73425 | 2025-10-18 04:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4cf5247c-c8b8-3e0c-9ea3-1fbc013629b6 | 1.76868 | -55.97756 | 2025-10-18 04:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 325e05ae-dcd6-32d6-bb17-7bbd8f7a4f64 | 1.75983 | -55.97509 | 2025-10-18 04:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 23c3b98c-54d6-375a-92b9-2021da8f3e6e | 2.02048 | -55.8336 | 2025-10-18 04:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1338f95d-37fc-37c8-b1be-8dcbf8937461 | 1.76134 | -55.74253 | 2025-10-18 04:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c10fbc7-e7c8-3c7e-a2c3-a8efcf613164 | -0.90473 | -47.54117 | 2025-10-18 04:46:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b4cfab31-f9e3-3858-ad76-0460b4b90ae9 | 1.76224 | -55.96333 | 2025-10-18 04:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f08ca936-adb3-3730-87b4-717a65b41c5d | 1.49787 | -56.05238 | 2025-10-18 04:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06322987-3e2a-3b36-a53e-94bbc42a18da | 1.76512 | -55.98193 | 2025-10-18 04:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8d7817eb-9987-3f81-9d3c-b9afbc1d1078 | 0.98066 | -51.18438 | 2025-10-18 04:46:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5df14a1-bf7e-379f-97ff-1037401f5fea | 0.99497 | -51.18921 | 2025-10-18 04:46:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59ffca1a-4766-3c9f-8649-45b80ce99e78 | 1.7681 | -55.97382 | 2025-10-18 04:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe525494-4a88-31b6-96dc-4dcf83024e3e | 2.01693 | -55.83795 | 2025-10-18 04:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19e05e9e-f013-33c5-8279-e8074fce85ca | 0.99828 | -51.18869 | 2025-10-18 04:46:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe2f7481-a9f1-3831-a19f-a22b0c2eaa05 | 1.09191 | -52.52183 | 2025-10-18 04:46:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a2d0171-3962-3b33-9fc1-b34eb40e7a1d | 1.7723 | -55.9465 | 2025-10-18 04:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba0f7e36-a3c7-300b-a7b0-870c71adf76a | -0.75716 | -47.76385 | 2025-10-18 04:46:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a536285-6631-3dc0-8f78-7ba750896c02 | 1.76531 | -55.92867 | 2025-10-18 04:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 98c6ee74-0bf2-3372-b669-75779e31e754 | 2.01637 | -55.83425 | 2025-10-18 04:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cca0daea-cc29-3e1c-af27-8e19b5dc7d53 | 1.75743 | -55.98689 | 2025-10-18 04:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5f29915-4590-3a18-96f8-046bfb5e378f | 1.77165 | -55.96946 | 2025-10-18 04:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d32bc6b-f502-36b8-9a46-a1ca06ae03be | 1.75628 | -55.97949 | 2025-10-18 04:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d85acf66-6e0b-30d6-8043-f1360753cd77 | 1.00159 | -51.18818 | 2025-10-18 04:46:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83b98e14-1599-320d-9717-67477b9cebd6 | 1.81732 | -55.70124 | 2025-10-18 04:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0aa2e43d-b422-36fb-acf6-7d19de79c944 | -6.40687 | -46.14467 | 2025-10-18 04:49:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 513c0e8d-ccb5-313f-bfb2-de1cbd740839 | -5.25665 | -50.90711 | 2025-10-18 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 95ef6240-296f-3d06-ba7e-8dc3eee232f9 | -2.74601 | -49.38953 | 2025-10-18 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7771ee79-7685-3910-96c1-8631643de48c | -8.36737 | -46.20593 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 886d5577-4cff-3f1e-ab09-b011f3aa5483 | -6.53767 | -55.05112 | 2025-10-18 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a07c831d-a5b4-3237-8a00-ddbd4d3aadd4 | -7.01356 | -55.2665 | 2025-10-18 04:49:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b172c8ad-ec96-3a32-b431-87d563516045 | -8.83025 | -49.66681 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e12bb24d-7b22-3a85-973a-4942488e6082 | -5.45583 | -45.40983 | 2025-10-18 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ac0eb350-eadf-3c7a-a0c4-4188ac954ec0 | -3.5054 | -52.89943 | 2025-10-18 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c724ff85-d0ec-3bf1-84f3-8d45603d08b6 | -4.52939 | -44.80087 | 2025-10-18 04:49:00 | NOAA-20 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20802649-4699-369b-bc87-3f66b3a5a663 | -6.23302 | -44.64742 | 2025-10-18 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f60a6d1-7340-311e-8e68-0889e6d0d7d8 | -7.11953 | -44.7343 | 2025-10-18 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b09f54a0-ec5b-3318-9427-464cd5e4610b | -2.73909 | -49.38849 | 2025-10-18 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e68d9989-31ab-34d6-be26-e1fc68cf3e23 | -2.86126 | -50.73863 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bfd79fa3-8cfc-3dce-985f-c1a5eaad997c | -8.35799 | -46.24103 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6181e055-778b-32aa-8534-589fb3fd759d | -7.76114 | -42.48629 | 2025-10-18 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| dc1bb57c-a062-3d1f-adea-cb89c642d614 | -7.35987 | -44.2279 | 2025-10-18 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e424a45-1f2a-3d5c-b0e8-9084cd2300b3 | -8.3574 | -46.24538 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb28edad-ae6f-3b46-a05f-69d088b4dc41 | -7.39499 | -46.97184 | 2025-10-18 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc83e1d1-e61e-3d14-b803-c1c15b451f9a | -7.79798 | -54.93901 | 2025-10-18 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 403fbd90-f186-3f05-a050-b227fbd5d504 | -7.15998 | -46.217 | 2025-10-18 04:49:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ff7882bd-d5a4-345b-839e-f759f912d02e | -5.16772 | -48.60671 | 2025-10-18 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 57a9a979-10b0-3155-8937-2ccb54afa585 | -9.14286 | -46.6668 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a39fff10-23fb-3560-84ba-7170a6b27954 | -9.55187 | -47.77134 | 2025-10-18 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 873bb60f-dfc7-3f96-ba16-330776441f91 | -9.66987 | -44.55059 | 2025-10-18 04:49:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 769b0fef-5988-3b6b-87c7-0631e906815d | -3.40754 | -46.89879 | 2025-10-18 04:49:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64ee669c-156c-3db4-99da-34f26528b20b | -4.49815 | -46.49025 | 2025-10-18 04:49:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 277d5c88-5765-34e9-911a-98c0301bfdce | -8.82704 | -49.68803 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42d81086-7ff9-37e4-a467-1a016205412c | -7.4721 | -42.7496 | 2025-10-18 04:49:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5c9e0b20-7273-3842-8374-76da8ccaf526 | -8.23392 | -44.00225 | 2025-10-18 04:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e0f31fc-f98a-384f-9427-108a4fbe1ecb | -3.05907 | -43.22028 | 2025-10-18 04:49:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b43ee604-8fb9-3369-bf7b-4055ef8d694a | -1.47443 | -55.82199 | 2025-10-18 04:49:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46b4226b-877b-3dd3-b0d9-00892bd2a3fb | -8.38327 | -49.73059 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c45ec9dc-7bb8-3739-a98f-7aa72057440c | -7.36752 | -44.2356 | 2025-10-18 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a4fc27f3-2b74-3e74-9aec-556d8862196d | -6.31388 | -44.32223 | 2025-10-18 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7747667c-83ae-3832-accb-178d95ab8c25 | -6.54397 | -43.9151 | 2025-10-18 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a4ed02f-d9fd-3efc-9ed7-52008a419d83 | -3.14415 | -50.25408 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 588e7aa3-cd73-3f25-8769-2cd65926026e | -8.35345 | -46.22466 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 181c50f2-3570-39a6-b470-c8dc7ebf3aec | -9.59081 | -47.85186 | 2025-10-18 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea1a7f46-c4b8-3ada-98c9-cdfc412f8591 | -7.76685 | -42.48726 | 2025-10-18 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a28d31a5-5d60-3cf8-ac67-99f30e752cd3 | -5.23784 | -49.85061 | 2025-10-18 04:49:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 915c91a1-0bc0-301c-8515-ff5b9f4d10e5 | -7.71431 | -47.84998 | 2025-10-18 04:49:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77a85332-9921-3d23-8fb1-41322864fa18 | -4.536 | -48.41033 | 2025-10-18 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 500c3f70-e8fc-383e-8855-95c804a13f67 | -5.89272 | -43.90042 | 2025-10-18 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ede833b8-6343-3dcd-b8b6-d68a24198566 | -3.33166 | -54.92253 | 2025-10-18 04:49:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa5278fb-b9c2-34b6-aadc-89c88782680a | -6.4791 | -42.16325 | 2025-10-18 04:49:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| dfe65cef-f5f8-378f-9f84-e483852d7b2f | -6.88663 | -45.45399 | 2025-10-18 04:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5fe95a4c-2584-3af0-80ae-44da11870db8 | -2.70656 | -49.86573 | 2025-10-18 04:49:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8897a37-409b-3471-8e6f-0848e2f049c4 | -4.44377 | -43.22463 | 2025-10-18 04:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README67.md)
